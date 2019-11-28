from random import seed
from random import randint
# declaring variables and lists
dice = [int(0),int(0),int(0),int(0),int(0)]
players = int(0)
reroll = int(2)
index = int(0)
keep = ""
variable = int(0)
player = int(0)
category = int(0)
cheater = int(0)
p1total = int(0)
p2total = int(0)
p3total = int(0)
p4total = int(0)
turns = int(1)
scorelist = [[int(-1) ,int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1)],[int(-1) ,int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1)],[int(-1) ,int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1)],[int(-1) ,int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1),int(-1)]]

# function for scoring first 6 options
def score_top(dice, scorelist, index, variable):
    if variable in dice:
        scorelist[index][variable-1] = int(dice.count(variable) * variable)
    else:
        scorelist[index][variable-1] = int(0)
        
# function for scoring other 7 options
def score_bot(dice, scorelist, index, variable):
    if variable == 7:
        if dice.count(1) >= 3 or dice.count(2) >= 3 or dice.count(3) >= 3 or dice.count(4) >= 3 or dice.count(5) >= 3 or dice.count(6) >= 3:
            scorelist[index][variable-1] = sum(dice)
        else:
            scorelist[index][variable-1] = int(0)
    if variable == 8:
        if dice.count(1) >= 4 or dice.count(2) >= 4 or dice.count(3) >= 4 or dice.count(4) >= 4 or dice.count(5) >= 4 or dice.count(6) >= 4:
            scorelist[index][variable-1] = sum(dice)
        else:
            scorelist[index][variable-1] = int(0) 
    if variable == 9:
        if (dice.count(max(dice)) == 3 and dice.count(min(dice)) == 2) or (dice.count(max(dice)) == 2 and dice.count(min(dice)) == 3):
            scorelist[index][variable-1] = int(25)
        else:
            scorelist[index][variable-1] = int(0)
    if variable == 10:
        if (1 in dice and 2 in dice and 3 in dice and 4 in dice) or (5 in dice and 2 in dice and 3 in dice and 4 in dice) or (5 in dice and 6 in dice and 3 in dice and 4 in dice):
            scorelist[index][variable-1] = int(30)
        else:
            scorelist[index][variable-1] = int(0) 
    if variable == 11:
        if (1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice) or (6 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice):
            scorelist[index][variable-1] = int(40)
        else:
            scorelist[index][variable-1] = int(0) 
    if variable == 12:
        scorelist[index][variable-1] = sum(dice)
    if variable == 13:
        if dice.count(1) == 5 or dice.count(2) == 5 or dice.count(3) == 5 or dice.count(4) == 5 or dice.count(5) == 5 or dice.count(6) == 5:
            scorelist[index][variable-1] = int(50)
        else:
            scorelist[index][variable-1] = int(0)  
            
# funtion for roling dice           
def roll_dice(dice, keep):
    if "1" not in keep:
        dice[0] = randint(1,6)
    if "2" not in keep:
        dice[1] = randint(1,6)
    if "3" not in keep:
        dice[2] = randint(1,6)
    if "4" not in keep:
        dice[3] = randint(1,6)
    if "5" not in keep:
        dice[4] = randint(1,6)     
        
# asking how many players are playing        
while players != 2 and players !=3 and players !=4:
    players = input("How many players are there (2-4 players): ")
    players = int(players)
    if players != 2 and players !=3 and players !=4:
        print("Your amount of players need to be between 2-4")
        
while turns < 14: # loop for the 13 turns
    print("Turn: " + str(turns))
    p1total = sum(scorelist[0]) + scorelist[0].count(-1)
    p2total = sum(scorelist[1]) + scorelist[1].count(-1)
    p3total = sum(scorelist[2]) + scorelist[2].count(-1)
    p4total = sum(scorelist[3]) +scorelist[3].count(-1)
    print("Scores - P1: " + str(p1total) + " P2: " + str(p2total) + " P3: " + str(p3total) + " P4: " + str(p4total))
   
    while index <= players - 1: # loop for each player 
        answer = input("Player " + str(index + 1) + " press enter to roll your dice: ")
        roll_dice(dice, keep)
       
        while reroll != 0: # loop for 2 rerolls
            print("dice 1 = " + str(dice[0]) + " \ndice 2 = " + str(dice[1]) + "\ndice 3 = " + str(dice[2]) + " \ndice 4 = " + str(dice[3]) + " \ndice 5 = " + str(dice[4]))
            answer = input("Press 1 to reroll \nPress 2 to add score to a category\n")
            if answer == "1":
                keep = input("Enter the dice you would like to keep (ex: 123): ")
                reroll = reroll - 1
                roll_dice(dice, keep)
            if answer == "2":
                reroll = 0
                
        while cheater == 0: # loop to make sure player does not select category more then once
            print("Your dice numbers are " + str(dice))
            print("Select a category the score your dice: \nPress 1 - Add up all the 1s \nPress 2 - Add up all the 2s \nPress 3 - Add up all the 3s")
            print("Press 4 - Add up all the 4s \nPress 5 - Add up all the 5s \nPress 6 - Add up all the 6s")
            print("Press 7 - Three of a kind - Add total of all 5 \nPress 8 - Four of a kind - Add total of all 5 \nPress 9 -  Full house - three of a kind + pair - 25 points")
            print("Press 10 - Small straight (1234, 2345, 3456) - 30 points \nPress 11 - Large straight (12345, 23456) - 40 points \nPress 12 - Chance - Add up the total of all 5 dice \nPress 13 - Yahtzee - 5 of a kind - 50 points") 
            answer = input("")
            variable = int(answer)
            if scorelist[index][variable-1] == -1:
                cheater = 1
            else:
                print("You already selected this category, Please select a new one")
        if variable > 0 and variable < 7:
            score_top(dice, scorelist, index, variable)
        if variable > 6 and variable < 14:
            score_bot(dice, scorelist, index, variable)
        print("You scored: " + str(scorelist[index][variable-1]))
        cheater = 0 
        index = index + 1
        reroll = 2
        keep = ""
    turns = turns + 1
    index = 0
    
# checking scores and outputting winner
p1total = sum(scorelist[0])
p2total = sum(scorelist[1])
p3total = sum(scorelist[2])
p4total = sum(scorelist[3])
if p1total > p2total and p1total > p3total and p1total > p4total:
    print("Player 1 is the winner with a score of " + str(p1total))
if p2total > p1total and p2total > p3total and p2total > p4total:
    print("Player 2 is the winner with a score of " + str(p2total))
if p3total > p2total and p3total > p1total and p3total > p4total:
    print("Player 3 is the winner with a score of " + str(p3total))
if p4total > p2total and p4total > p1total and p4total > p3total:
    print("Player 4 is the winner with a score of " + str(p4total))
print("Scores - P1: " + str(p1total) + " P2: " + str(p2total) + " P3: " + str(p3total) + " P4: " + str(p4total))