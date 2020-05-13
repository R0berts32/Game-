import sys
# Creating How Many players in the game

Player_1 = input('Player 1 insert a battle name!')
Player_2 = input('Player 2 insert a battle name!')
user1_answer = input("%s, Will you like to choose Rock , Paper, or Scissors?" % Player_1)
user2_answer = input("%s, Will you like to choose Rock , Paper, or Scissors?" % Player_2)
############

# Programming Game
def compare (P1 , P2):
    if P1 == P2:
        return("Its a tie!")
    elif P1 == 'Rock':
        if P2 == 'Scissors' :
            return("Rock Wins!")
        else:
            return("Paper Wins!")
    elif P1 == 'Scissors':
        if P2 == "Paper" :
            return("Scissors Win!")
        else:
            return("Rock Wins!")
    elif P1 == 'Paper' :
        if P2 == 'Rock' :
            return("Paper Wins!")
        else:
            return("Sissors Win!")
    else:
        return("Invalid Input! You Have to choose Rock , Paper , Or Scissors")