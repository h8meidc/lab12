import json
teams = [{"Name"        : "Beastcoast",
             "Points"     : 100,},
            {"Name"        : "GG",
             "Points"     : 45,},
            {"Name"        : "Teamteam",
             "Points"     : 54,},
            {"Name"        : "NAVI",
             "Points"     : 78,}]
jsonData = json.dumps(teams)
with open("data.json", "wt") as file:
    file.write(jsonData)
file.close
while True:    
    print("Select an option:\n 1 - Add data\n 2 - Delete data\n 3 - View data\n 4 - Find team for name\n 5 - Show 1th,2th and 3th places\n 6 - Exit") 
    x = input("Choose an option:\n") 
    x = int(x)
    if x == 1:
        with open("data.json", "w") as file:
            teams = json.loads(jsonData)
            print("Add: ")
            name = input("Name:")
            points = int(input("Points:"))
            teams.append({"Name": name, "Points": points})
            jsonData = json.dumps(teams)
            print(f"Team {name} added.")
            file.write(jsonData)
            file.close()

    elif x == 2:
        with open("data.json", "w") as file:
            teams = json.loads(jsonData)
            length = len(teams)
            name = input("Name:")
            teams = [team for team in teams if team["Name"] != name]
            jsonData = json.dumps(teams)
            if len(teams) < length:
                print(f"Team {name} deleted.")
            else:
                print(f"Team {name} not found.")
            file.write(jsonData)
            file.close()
    elif x == 3:
        with open("data.json", "rt") as file:
            teams = json.loads(jsonData)
            print(*teams, sep='\n')
    elif x == 4:
        with open("data.json", "rt") as file:
            teams = json.loads(jsonData)
            name = input('Name of team: ')
            result = [team for team in teams if team["Name"].lower() == name.lower()]
            if result:
                print(*result, sep='\n')
            else:
                print(f"Team {name} not found.")
    elif x == 5:
        with open("data.json", "rt") as file:
            teams = json.loads(jsonData)
            sorted_teams = sorted(teams, key=lambda x: x["Points"], reverse=True)
            first_place = sorted_teams[0]["Name"]
            second_place = sorted_teams[1]["Name"]
            third_place = sorted_teams[2]["Name"]
            print(f"First place: {first_place}")
            print(f"Second place: {second_place}")
            print(f"Third place: {third_place}")

    elif x == 6:
        quit(0)
    else:
        print("Incorrect action.")
