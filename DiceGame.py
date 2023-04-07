"""
Rules: 
    Eeach player in turn rolls a dice.
    If the dice is equal to one, it is the next player's turn.
    Any player who reaches 50 point wins
    
    You are allowed to select at least two and up to four players.
    Also, at least one player must be a human,
    otherwise the defualt mode of one human and one computer will be considered for you.
"""


from random import randint
from termcolor import colored
from os import system
from time import sleep


players = {
    "player1" : {"name": "player1", "score": 0, "turn": True},
}


def won(plyrs, trn):
    if plyrs[trn]["score"] >= 50:
        return True , plyrs[trn]
    
    return False, None
        
    
def print_dice(dc, score):
    
    j = 0
    for i in dc:
        end = " "
        j += 1
        if j % 3 == 0:
            end = "\n"
        if score == 1:
            print(colored(i, "red"), end=end)
        else:
            print(i, end=end)
    

def change_turn(plyrs):
    r = 0
    key = None
    
    for plyr in plyrs.values():
        r += 1
        
        if plyr['turn']:
            plyr["turn"] = False
            
            if len(players) > r:
                key = r + 1
            else:
                plyrs["player1"]["turn"] = True
                break
        if key == r:
            plyr["turn"] = True


def players_score(score, trn, plyrs):
    if score == 1:
        return
    
    plyrs[trn]["score"] += score


def players_move(plyrs, dc):
    if dc == 1:
        change_turn(plyrs)
        
    for i in plyrs.keys():
        if plyrs[i]['turn']:
            turn = i
            
    if turn[0:8] == 'computer':
        return turn, False
    return turn, True
        
        
def print_players_score(plyrs, trn):
    for i in plyrs.values():
        if trn == i["name"]:
            print(colored("{} : {}".format(i["name"], i["score"]), "green"), end="\t")
        else:
            print("{} : {}".format(i["name"], i["score"]), end="\t")

       
def add_players(plyrs):
    all_num_players = int(input(colored("enter the number of players you want: ", "yellow")))
    num_computers = int(input(colored("enter the number of players who are computer: ", "yellow")))

    if all_num_players > 4 or num_computers > 3 or all_num_players <= num_computers:
        all_num_players = 2
        num_computers = 1
        
    num_players = all_num_players - num_computers
    
    for i in range(2, all_num_players+1):
        if i < num_players+1:
            plyrs["player{}".format(i)] = {"name": "player{}".format(i), "score": 0, "turn": False}
        else:
            plyrs["computer{}".format(i-num_players)] = {"name": "computer{}".format(i-num_players), "score": 0, "turn": False}


add_players(players)
win, user_play = False, True        

while not win:   
    if user_play:
        input(colored("\nenter to drop dice: ", "yellow"))
        system("cls")
        print("droping dice...")
        sleep(1)
    else: 
        print(colored("\nwait for your turn...", "yellow"))
        sleep(2)
    
    system("cls")
    random_number = randint(1, 5)
    dice = f"----{random_number}----"
    print_dice(dice, random_number)
    turn, user_play = players_move(players, random_number)
    players_score(random_number, turn, players)
    print_players_score(players, turn)
    win, winner = won(players, turn)
    
    if win:
        print(colored("\n{} is win with {} score.".format(winner["name"], winner["score"]), "green"))