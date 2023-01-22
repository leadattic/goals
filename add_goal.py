import json

print("""

Welcome to Create goal
""")
name = input("What do you want the name of the goal to be?  ")
reward=input("What should the reward be?  ")
type = input("""
What type of goal?

(1) chess.com elo
""")


def program():
    if type == '1':
        gamemode = input(
"""
NOTE: if you have not yet, you have to add your chess.com username to "chesscomuser" in config.json
(1)Rapid (2)Blitz (3)Bullet
"""
        )
        if gamemode == '1':
            elo=int(input("What amount of elo"))
            goaldict = {
                "name": f"{name}",
                "reward": f"{reward}",
                "type": "rapid_elo",
                "criteria": elo
            }

            goal = json.load(open("goal.json"))

            goal['goals'].append(goaldict)

            fl = open("goal.json", "w")
            fl.write(json.dumps(goal))
            fl.close()

        if gamemode == '2':
            elo=int(input("What amount of elo "))
            goaldict = {
                "name": f"{name}",
                "reward": f"{reward}",
                "type": "blitz_elo",
                "criteria": elo
            }

            goal = json.load(open("goal.json"))

            goal['goals'].append([goaldict])

            fl = open("goal.json", "w")
            fl.write(json.dumps(goal))
            fl.close()

        if gamemode == '3':
            elo=int(input("What amount of elo"))
            goaldict = {
                "name": f"{name}",
                "reward": f"{reward}",
                "type": "bullet_elo",
                "criteria": elo
            }
            goal = json.load(open("goal.json"))

            goal['goals'].append([goaldict])

            fl = open("goal.json", "w")
            fl.write(json.dumps(goal))
            fl.close()



if int(type) < 2:
    program()
else:
    print('Invalid choise: press enter to quit')
    input()




