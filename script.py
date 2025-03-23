import requests

username = input("Enter username: ")
url = f"https://api.github.com/users/{username}/events"

response = requests.get(url)
map = {}
if response.status_code == 404:
  print("User not found?")

elif response.status_code == 200:
  events = response.json()
  for event in events:
    if event['type'] == 'PushEvent':
      repo = event['repo']['name']
      if repo not in map:
        map[repo] = 0
      else:
        map[repo] += 1
    if event['type'] == 'WatchEvent':
      print(f"Watch event created for repo {event['repo']['name']}")
    if event['type'] == 'IssueCommentEvent':
      print(f"IssueComment event created for repo {event['repo']['name']} with message {event['payload']['issue']['title']}")


for key, value in map.items():
  print(f"You commited to {key} {value} many times. \n") 
