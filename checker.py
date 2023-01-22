import json
import time
import chessdotcom as cc
from win10toast import ToastNotifier


#data = cc.get_player_stats("leadattic").json
#print(data['stats']['chess_rapid']['last']['rating'])

config = json.load(open("config.json"))
notifier = ToastNotifier()

# notifier.show_toast(f"You reached the goal \"{goal}\"", f"Your reward is {reward}", duration=10, threaded=True)

while True:
    goals = json.load(open("goal.json"))
    for i in range(len(goals['goals'])):

        if goals['goals'][i]['type'] == 'rapid_elo':
            if cc.get_player_stats(config["chesscomuser"]).json['stats']['chess_rapid']['last']['rating'] >= goals['goals'][i]["criteria"]:
                notifier.show_toast(f"You reached the goal \"{goals['goals'][i]['name']}\"", f"Your reward is {goals['goals'][i]['reward']}", duration=10000000,threaded=True)
                goals['goals'].remove(goals['goals'][i])
                fl = open("goal.json", "w")
                fl.write(json.dumps(goals))
                fl.close()

        if goals['goals'][i]['type'] == 'blitz_elo':
            if cc.get_player_stats(config["chesscomuser"]).json['stats']['chess_blitz']['last']['rating'] >= goals['goals'][i]["criteria"]:
                notifier.show_toast(f"You reached the goal \"{goals['goals'][i]['name']}\"", f"Your reward is {goals['goals'][i]['reward']}", duration=10000000,threaded=True)
                goals['goals'].remove(goals['goals'][i])
                fl = open("goal.json", "w")
                fl.write(json.dumps(goals))
                fl.close()

        if goals['goals'][i]['type'] == 'bullet_elo':
            if cc.get_player_stats(config["chesscomuser"]).json['stats']['chess_bullet']['last']['rating'] >= goals['goals'][i]["criteria"]:
                notifier.show_toast(f"You reached the goal \"{goals['goals'][i]['name']}\"", f"Your reward is {goals['goals'][i]['reward']}", duration=10000000,threaded=True)
                goals['goals'].remove(goals['goals'][i])
                fl = open("goal.json", "w")
                fl.write(json.dumps(goals))
                fl.close()

    time.sleep(config['update_rate'])
