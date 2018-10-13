#!/usr/bin/env python

# The Tic-Tac-Toe-Tomek

def readgame(f):
    game = []
    for i in range(0,4):
        game.append(f.read(4))
        f.read(1)
    f.read(1)    
    return game

def is_game_complete(game):
    for row in game:
        if row.find('.') >= 0:
            return False
    return True

def search_game(game,player,p,d,l):
    
    #print 'p', p, 'l', l
    
    if game[p[1]][p[0]] == player or game[p[1]][p[0]] == 'T':
        new_p = (p[0]+d[0],p[1]+d[1])
        l = l + 1
        if l == 4:
            return True
        return search_game(game,player,new_p,d,l)        
    else:
        return False

# search start positions and directions
sp = [(0,0), (0,0), (0,1), (0,2), (0,3), (0,0), (1,0), (2,0), (3,0), (0,3)]
ds = [(1,1), (1,0), (1,0), (1,0), (1,0), (0,1), (0,1), (0,1), (0,1), (1,-1)]

def is_win(game, player):
    
    win = False
    test = 0
    
    while not win and test < len(sp):
        win = search_game(game,player,sp[test],ds[test],0)
        test = test + 1
        
    return win
    
    # Full hard coded search
    '''
    win = False
    
    # search diagonal
    win = win or search_game(game,player,(0,0),(1,1),0)       
    
    # search horizontal
    win = win or search_game(game,player,(0,0),(1,0),0)
    win = win or search_game(game,player,(0,1),(1,0),0)               
    win = win or search_game(game,player,(0,2),(1,0),0)
    win = win or search_game(game,player,(0,3),(1,0),0)

    # search vertical
    win = win or search_game(game,player,(0,0),(0,1),0)
    win = win or search_game(game,player,(1,0),(0,1),0)               
    win = win or search_game(game,player,(2,0),(0,1),0)
    win = win or search_game(game,player,(3,0),(0,1),0)

    # search diagonal
    win = win or search_game(game,player,(0,3),(1,-1),0)

    return win
    '''

def main():
    
    #f = open('input.txt', 'r')
    #f = open('A-small-attempt2.in', 'r')
    f = open('A-large.in', 'r')
    T = int(f.readline())
    
    out = open('output.txt', 'w')
    
    for i in range(T):
        game = readgame(f)
        if is_win(game,'X'):            
            out.write('Case #'+str(i+1)+': X won\n')
        elif is_win(game, 'O'):
            out.write('Case #'+str(i+1)+': O won\n')
        elif not is_game_complete(game):
            out.write('Case #'+str(i+1)+': Game has not completed\n')     
        else:
            out.write('Case #'+str(i+1)+': Draw\n')
    return
       
if __name__ == '__main__': 
    main()
