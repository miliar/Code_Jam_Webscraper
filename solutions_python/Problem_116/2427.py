#
# Code by Fernando Gil <http://www.fernandogil.com.br> for Google Code Jam 2013
#
# Use:
# $python tictactoe.py sample.in
#
#
import sys

def check(a,b,c,d):
    playerX = 0
    playerO = 0
    plays = [board[a],board[b],board[c],board[d]]
    for play in plays:
        if(play == 'X'):
            playerX = playerX + 1
        elif(play == 'O'):
            playerO = playerO + 1
        elif(play == 'T'):
            playerX = playerX + 1
            playerO = playerO + 1
    
    if(playerX == 4):
        sys.stdout.write('X won\n')
        return True
    elif(playerO == 4):
        sys.stdout.write('O won\n')
        return True
    else:
        return False
      
# MAIN

state = 0
line = 0

filename = sys.argv[1]
file = open(filename, 'r')

cases = int(file.readline()) # cases line

for case in range(1,cases+1):
    sys.stdout.write('Case #%d: ' % case)
    isCompleted = True
    board = []
    result = False
    for i in range(16):
        c = file.read(1)
        if ord(c) == 10:
            c = file.read(1)
        
        if(c == '.'):
            isCompleted = False
            
        board.append(c)
        
        if (i==3):
            result = check(0,1,2,3)
        elif (i==7):
            result = check(4,5,6,7)
        elif (i==11):
            result = check(8,9,10,11)
        elif (i==12):
            result = check(3,6,9,12)
            result = result or check(0,4,8,12)
        elif (i==13):
            result = check(1,5,9,13)
        elif (i==14):
            result = check(2,6,10,14)
        elif (i==15):
            result = check(3,7,11,15)
            result = result or check(0,5,10,15)
            result = result or check(12,13,14,15)
            
        if result:
            file.read(15-i)
            break
    
    if(not result):
        if(isCompleted):
            sys.stdout.write('Draw\n')
        else:
            sys.stdout.write('Game has not completed\n')
        
    file.readline() # blank line
    
    