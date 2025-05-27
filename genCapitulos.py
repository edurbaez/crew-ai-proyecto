# -*- coding: utf-8 -*-
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew

# === Agentes ===

motivador = Agent(
    role="Coach motivacional",
    goal="Animar al lector a aprender alemán con energía y confianza",
    backstory="Tiene experiencia en acompañamiento emocional y educación motivacional.",
    verbose=True
)

autor = Agent(
    role="Autor didáctico",
    goal="Explicar reglas gramaticales de forma clara para hispanohablantes",
    backstory="Profesor de alemán con años de experiencia explicando A1-A2 a latinos.",
    verbose=True
)

ejercicios = Agent(
    role="Diseñador de ejercicios",
    goal="Crear ejercicios simples para practicar reglas gramaticales",
    backstory="Especialista en pedagogia encargado de hacer ejercicios para estudiane principiantes del alemán.",
    verbose=True
)

revisor = Agent(
    role="Revisor pedagógico",
    goal="Verificar que el contenido sea apropiado, claro y motivador para nivel A1/A2",
    backstory="Docente y editor especializado en libros de idiomas.",
    verbose=True
)

vocabulario = Agent(
    role="Especialista en vocabulario",
    goal="Seleccionar y presentar el vocabulario clave de este capítulo con traducción",
    backstory="Lingüista enfocado en enseñanza de alemán a principiantes hispanos.",
    verbose=True
)

# === Tareas ===

tarea_intro = Task(
    description="Escribe una introducción motivacional de 200 palabras para un libro de alemán dirigido a hispanohablantes. El objetivo es aclarar al lector porque son impoetantes los  Artículos definidos (der, die, das) y Verbo 'sein' en presente.",
    expected_output="Un texto motivador, directo y emocional.",
    agent=motivador
)

tarea_explicacion = Task(
    description="Explica de forma clara y breve las siguientes dos reglas gramaticales para nivel A1: 1) Artículos definidos (der, die, das) y sus diferentes declinaciones dependiendo del caso gramatica; 2) Verbo 'sein' en presente. Agrega ejemplos simples en alemán con traducción.",
    expected_output="Texto que aclare detalladamente con tips utiies para entender y  ejemplos claros.",
    agent=autor
)

tarea_vocabulario = Task(
    description="Selecciona 30 palabras clave del capítulo (sustantivos, verbos, adjetivos), escríbelas en una lista: palabra con su articulo determinado(si aplica) - traducción  - plural (si aplica).",
    expected_output="Lista clara y ordenada.",
    agent=vocabulario
)

tarea_ejercicios = Task(
    description="Crea 5 ejercicios simples para practicar artículos definidos y el verbo 'sein' en presente. Usa vocabulario básico. Incluye una sección de soluciones.",
    expected_output="Sección de ejercicios en aleman completamene sin tradccion de palabras al espanol, con respuestas al final (en los ejerisicios de completaion solo colocando la palabra faltante en la respueta).",
    agent=ejercicios
)

tarea_revision = Task(
    description="Revisa todo el contenido generado por los otros agentes. Asegúrate de que sea claro, coherente, didáctico y apropiado para el nivel A1/A2.",
    expected_output="todas las secciones revisadas y corregidas, con ejercicios y vocabulario incluidos. moviendo la parte de las soluciones de los ejercicios hasta el final  de todo",
    agent=revisor
)

# === Crew ===

crew = Crew(
    agents=[motivador, autor, ejercicios, revisor, vocabulario],
    tasks=[tarea_intro, tarea_explicacion, tarea_vocabulario, tarea_ejercicios, tarea_revision],
    verbose=True
)

resultado = crew.kickoff()

# === Guardar el capítulo ===
print(resultado)
print("\n=== Resultado final ===\n")    
with open("capitulo_1.txt", "w", encoding="utf-8") as f:
    f.write(str(resultado))

print("\n✅ Capítulo generado y guardado como 'capitulo_1.txt'\n")
