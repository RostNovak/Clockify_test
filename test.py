import requests
import pandas as pd

api_key='NWZkMzViMmEtOGEzOS00NTg1LTgxNGItY2UxZTY1YzUzMGFl'
data = {'x-api-key': api_key}


r = requests.get('https://api.clockify.me/api/v1/user', headers=data)
userId = r.json()["id"]
workspaceId = r.json()["activeWorkspace"]
r = requests.get(f'https://api.clockify.me/api/v1/workspaces/{workspaceId}/user/{userId}/time-entries', headers=data)

df = pd.DataFrame(columns = ['id',"description","start",'end','duration'])
for i in range(len(r.json())):
    df.loc[i,'id'] = r.json()[i]['id']

for i in df.index:
    id = df.loc[i]['id']
    r = requests.get(f'https://api.clockify.me/api/v1/workspaces/{workspaceId}/time-entries/{id}',
                     headers=data)
    df.loc[i, 'description'] = r.json()['description']
    df.loc[i, 'start'] = r.json()['timeInterval']['start']
    df.loc[i, 'end'] = r.json()['timeInterval']['end']
    df.loc[i, 'duration'] = r.json()['timeInterval']['duration']
pd.set_option('max_columns', None)
print(df)