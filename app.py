import constants
import copy


players = copy.deepcopy(constants.PLAYERS)
teams   = copy.deepcopy(constants.TEAMS)
Panthers  = []
Bandits   = []
Warriors  = []
experince_player   = []
inexperince_player = []


def main_app():
    print("BASKETBALL TEAM STATS TOOL\n---- MENU----\nHere are your choices:\nA) Display Team Stats\nB) Quit\n")
    while True:
        option = input("Enter an option please: ")
        if option.lower() == "b":
          print('Exit')
          break
        elif option.lower() == "a":
            print("A) Panthers\nB) Bandits\nC) Warriors\n")
            while True:
                option2 = input("Enter an option please: ")
                if option2.lower() == "a":
                    stats(Panthers,"Panthers")
                elif option2.lower() == "b":
                    stats(Bandits,"Bandits") 
                elif option2.lower() == "c":
                    stats(Warriors,"Warriors") 
                else:
                    print("Please enter valid choice!\n")           
        else:
            print("Please enter valid choice!\n") 


def clean_data():
    for player in players:
        player['height'] = int(player['height'].split()[0])
        experience = player['experience'].split()
        if experience[0] == "YES":
            player['experience'] = True
            experince_player.append(player)
        else:
            player['experience'] = False
            inexperince_player.append(player)
        player["guardians"] = player["guardians"].split("and")    


def balance_teams():
    num_explayers_team = int(len(experince_player)/len(teams))
    num_inexplayers_team = int(len(inexperince_player)/len(teams))
    sum_players = num_explayers_team + num_inexplayers_team
    for player in experince_player:
        if len(Panthers) < num_explayers_team :
            Panthers.append(player)
        elif len(Bandits) < num_explayers_team:
            Bandits.append(player)
        else:
            Warriors.append(player)
    for player in inexperince_player:
        if len(Panthers) < sum_players :
            Panthers.append(player)
        elif len(Bandits) < sum_players:
            Bandits.append(player)
        else:
            Warriors.append(player)         
   

def stats(team,name_team):
    players_name = []
    guardians = []
    new_guardians = []
    num_exp_players   = 0
    num_inexp_players = 0
    sum_height = 0
    for player in team:
        sum_height += player["height"]
        if player["experience"] == True:
            num_exp_players   += 1
        else:
            num_inexp_players += 1       
    print("\n")
    print("Team: {} stats".format(name_team))
    print("---------------------")
    print("Total players: {}\n".format(len(team)))
    print("Total experienced: {}\n".format(num_exp_players))
    print("Total inexperienced: {}\n".format(num_inexp_players))
    print("Average height: {}\n".format(sum_height/len(team)))
    for name in team:
        players_name.append(name['name'])
    print("Players on Team:")
    print(', '.join(players_name))
    print("\n")
    for guar in team:
        guardians.append(guar['guardians'])
    print("Guardians:")
    for items in guardians:
        for item in items:
            new_guardians.append(item)  
    print(', '.join(new_guardians))
    print("\n")
    input("Press Enter to continue...\n")
    main_app()


if __name__ == '__main__': 
    clean_data()
    balance_teams()
    main_app()
