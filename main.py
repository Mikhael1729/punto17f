from packages.data_structures import Graph
from letters_agent import LettersAgent
from colors_agent import ColorsAgent

agent = ColorsAgent()
exists = agent.state_exists_gbfs(['red', 'blue', 'green', 'red'])

print("exists: ", exists[0])
print("path: ")

for node in exists[1]:
  print("  - ", node)

