import requests

api_key='NWZkMzViMmEtOGEzOS00NTg1LTgxNGItY2UxZTY1YzUzMGFl'
data = {'x-api-key': api_key}


r = requests.get('https://api.clockify.me/api/v1/user', headers=data)
userId = r.json()["id"]
workspaceId = r.json()["activeWorkspace"]
r = requests.get(f'https://api.clockify.me/api/v1/workspaces/{workspaceId}/user/{userId}/time-entries', headers=data)
print(r.content)
