import json

with open('players.json') as f:
  data = json.load(f)

for teams in data['teams']:
  del teams['country']

with open('new_players.json', 'w') as f:
  json.dump(data, f, indent=2)