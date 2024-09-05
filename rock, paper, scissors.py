import random

def play():
    user = input(" Choose: 'r' for rock, 'p' for paper and 's' for scissor  ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie!'
    
    if is_win(user,computer):
        return 'You won!'
    
    if is_win(computer,user):
        return "You lost!"
    
def is_win(player,opponent):
    if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print (play())
         