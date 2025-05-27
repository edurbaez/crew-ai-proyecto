# -*- coding: utf-8 -*- 
from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Task, Crew 
 
writer = Agent( 
    role="Redactor de noticias", 
    goal="Escribir un artculo claro y atractivo sobre inteligencia artificial", 
    backstory="Trabaja en un medio digital con experiencia en tecnologa.", 
    verbose=True 
) 
 
article_task = Task(
    description="Escribe un artículo de 3 párrafos explicando qué es la inteligencia artificial y por qué es importante hoy.",
    expected_output="Un texto bien escrito de tres párrafos, claro, informativo y con un tono profesional.",
    agent=writer
) 
crew = Crew( 
    agents=[writer], 
    tasks=[article_task], 
    verbose=True 
) 
 
resultado = crew.kickoff() 
with open("resultado.txt", "w", encoding="utf-8") as f:
    f.write(resultado)
print("\n=== Resultado final ===\n") 
print(resultado) 


