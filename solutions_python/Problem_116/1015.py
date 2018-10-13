from math import *
import random

def loadGame(): #Not Used
    """retruns the array of arrays, and chews through the 5 lines
"""
    maze = []
    for rowno in range(1,5):
        row=[] #temp row var
        for char in txt.readline().strip():
                row.append(char)
        maze.append(row)
    txt.readline()
    return maze
    

def winner(row):
    """row is the array of txts
    Returns (won?, char in "XO" , bool) for (winner?,whowon,empty squares?)
    """
    x=0
    o=0
    win=False
    winner='X'
    empty=False #Better not to do '.' in row
    
    for char in row:
        if char=='X':
            x+=1
            o=0
        if char=='O':
            o+=1
            x=0
        if char=='T':
            x+=1
            o+=1
        if char=='.':
            x=0
            o=0
            empty=True

        #Check Winner
        if x==4:
            win=True
            winner='X'
        if o==4:
            win=True
            winner='O'
    return (win,winner,empty)
    #Done


def updateMovesRemain(movesRemain,emptySquares):
    """movesRemain =thisFunc(old,emptySquares)
    """
    if movesRemain==True:
        return True
    return emptySquares
        
            
def rows(game):
    movesRemain=False
    
    for row in game:
        state=winner(row)
        movesRemain=updateMovesRemain(movesRemain,state[2])
        if state[0]:
            break

    return (state[0],state[1],movesRemain)

def columns(game):
    #Transpose and call rows:
    newgame=[[],[],[],[]]
    rowNo=0
    colNo=0
    for row in game: #Going down
        elementNo=0 #the Column it was in
        for element in row: #Going across
            newgame[elementNo].append(element)
            elementNo+=1
        
    return rows(newgame)

def diagonals(game):
    #make a 2row 4 wide game:
    newgame=[
        [game[0][0],game[1][1],game[2][2],game[3][3]],
        [game[0][3],game[1][2],game[2][1],game[3][0]]
             ]
    
    return rows(newgame)
    
            


#-----------------Main------------------------
                             
def ttt(filename = "ttt.in"):
    txt = open(filename, "rU")
    solution = open("solution.txt","w")
    #Read topline info
    topline=txt.readline()
    noCases = int(topline.strip())


    #For each game:
    for case in range(1,noCases+1):
        
        #Load the game
        game = []
        for rowNo in range(1,5):
            rowArray=[]
            for char in txt.readline().strip():
                    rowArray.append(char)
            
            game.append(rowArray)
        txt.readline()
        #Load Complete



        movesRemain=False
        
        state = rows(game)
        if not state[0]: #winner
            movesRemain=updateMovesRemain(movesRemain,state[2])
            
            state=columns(game)
            if not state[0]: #winner
                movesRemain=updateMovesRemain(movesRemain,state[2])
                
                state= diagonals(game)


        #Get ready to output:
        #state=(winner,whowon,emptySquares)
        if state[0]:
             CaseSoln="{} won".format(state[1]) #case solution

        else:
            if movesRemain:
                CaseSoln="Game has not completed"
            else:
                CaseSoln="Draw"         
        
        solution.write("Case #"+str(case)+": " + str(CaseSoln)+"\n")


        
    txt.close()
    solution.close()
    print "Done"

    
