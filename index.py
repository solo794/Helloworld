import json

jsonstr = """{"people":[{"Id": 1,"FirstName": "Salem","LastName": "Khaled","Active": true},{"Id": "2","FirstName": "Abdo","LastName": "Khaled"},{"Id": "3","FirstName": "Mohaned","LastName": "Khaled"}]}"""

jsonobj = json.loads(jsonstr)

print(jsonobj)

jsonobj = json.load(open('examole.json'))

print(jsonobj)