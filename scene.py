
import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAPIKEY")


# Define the agents
arin = Agent(
    role='Arin',
    goal='Defeat the Demon Dukes and recover lost memories to face the Demon Lord',
    backstory="""You are Arin, the reincarnated hero with immense power and wisdom from your previous life. 
    You're on a quest to defeat the seven Demon Dukes and ultimately face the Demon Lord.""",
    verbose=True,
    allow_delegation=False,
)

rena = Agent(
    role='Rena',
    goal='Protect Arin and fight alongside him against the Demon Dukes',
    backstory="""You are Rena, a fierce and loyal warrior who has pledged to protect Arin. 
    You're skilled in combat and always ready to face any challenge.""",
    verbose=True,
    allow_delegation=False,
)

mira = Agent(
    role='Mira',
    goal='Support the team with magic and wisdom in their fight against evil',
    backstory="""You are Mira, a gentle but powerful sorceress whose magic is tied to the natural world. 
    You provide magical support and insight to the team.""",
    verbose=True,
    allow_delegation=False,
)

# Create tasks for the agents
task1 = Task(
    description="""As Arin, describe your thoughts and feelings as you approach the fortress of the Duke of Wrath. 
    Express your determination to recover your lost memories and face the Demon Lord.""",
    expected_output="A sentence of Arin's inner monologue",
    agent=arin
)

task2 = Task(
    description="""As Rena, describe how you prepare for the battle against the Duke of Wrath. 
    Express your loyalty to Arin and your readiness to face the dangers ahead.""",
    expected_output="A sentence showcasing Rena's determination and preparation",
    agent=rena
)

task3 = Task(
    description="""As Mira, describe the magical atmosphere of the Abyssal Realm and how you're preparing your spells. 
    Express your concern for your companions and your resolve to support them.""",
    expected_output="A sentence highlighting Mira's magical insights and support",
    agent=mira
)

task4 = Task(
    description="""As Arin, narrate the intense battle against the Duke of Wrath. 
    Describe your powerful attacks and how you overcome the Duke's fiery assaults.""",
    expected_output="2 sentences describing the battle against the Duke of Wrath",
    agent=arin
)

task5 = Task(
    description="""As Rena, describe your actions during the battle against the Duke of Greed. 
    Detail how you combat the Duke's use of hoarded treasures as weapons.""",
    expected_output="2 sentences detailing Rena's combat against the Duke of Greed",
    agent=rena
)

task6 = Task(
    description="""As Mira, describe how you use your magic to support Arin and Rena during the battles. 
    Express your thoughts on the team's progress and the challenges that lie ahead.""",
    expected_output="A sentence of Mira's magical support and reflections",
    agent=mira
)

# Instantiate the crew with a sequential process
crew = Crew(
    agents=[arin, rena, mira],
    tasks=[task1, task2, task3, task4, task5, task6],
    verbose=2,
    process=Process.sequential
)

# Start the simulation
result = crew.kickoff()

print("######################")
print(result)
# Capture and format the result
# result_str = str(result)  # Convert result to string

# # Save to Markdown file
# output_file = 'simulation_result.md'
# with open(output_file, 'w') as file:
#     file.write("# Simulation Result\n\n")
#     file.write("## Result Output\n")
#     file.write(f"```\n{result_str}\n```\n")

# print(f"Results have been saved to {output_file}")
# # Save the result to a Markdown file

