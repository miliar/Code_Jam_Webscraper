'''
Created on 2013. 4. 13.

@author: purepleya
'''

def solve():
    f = open('A-large.in', 'r') 
    out_file = open('A-large.out', 'w')
    
    lines = f.readlines()
    index = 0
    game_count = 0
    game_index = 1
    line_index = 0
    
    game = []
    
    for line in lines:
        if index > 0: 
            if line != '\n':
                game.append(line.replace('\n', ''))
                line_index += 1
    
                if line_index == 4:
#                    print game
                    out_file.write('Case #%d: %s' % (game_index, check(game)))
                    
                    out_file.write('\n')
                    game_index += 1
                    line_index = 0
                    game = []
            
        index = index + 1
    f.close()
    out_file.close()

    

def check(game):
    reslt = ''
    cnt_O = 0
    cnt_X = 0
    cnt_T = 0
    cnt_dot = 0
    
    for line in game:
        cnt_O += line.count('O')
        cnt_X += line.count('X')
        cnt_T += line.count('T')
        cnt_dot += line.count('.')
    
    for row in range(0, 4):
        tempPlayer = game[row][0]
        if tempPlayer == 'T' : tempPlayer = game[row][1]
        for col in range(0, 4):
            if game[row][col] == '.': break
            if tempPlayer == game[row][col] or game[row][col] == 'T':
                if col == 3: 
                    if reslt != tempPlayer: reslt += tempPlayer
            else: break
    
    for col in range(0, 4):
        tempPlayer = game[0][col]
        if tempPlayer == 'T' : tempPlayer = game[1][col]
        for row in range(0, 4):
            if game[row][col] == '.': break
            if tempPlayer == game[row][col] or game[row][col] == 'T':
                if row == 3: 
                    if reslt != tempPlayer: reslt += tempPlayer
            else: break
    
    
    tempPlayer = game[0][0]
    if tempPlayer == 'T' : tempPlayer = game[1][1]
    for index in range(0, 4):
        if game[index][index] == '.': break
        if tempPlayer == game[index][index] or game[index][index] == 'T':
            if index == 3 : 
                if reslt != tempPlayer: reslt += tempPlayer
        else: break
    
    tempPlayer = game[0][3]
    if tempPlayer == 'T' : tempPlayer = game[1][2]
    for index in range(0, 4):
        if game[index][3 - index] == '.': break
        if tempPlayer == game[index][3 - index] or game[index][3 - index] == 'T':
            if index == 3 : 
                if reslt != tempPlayer: reslt += tempPlayer
        else: break
    
    if reslt.__len__() > 1 :
        return 'DRAW'
    elif reslt.__len__() == 1:
        return reslt + ' won'
    else:
        if cnt_O + cnt_X + cnt_T == 16 : 
            return 'Draw'
        else:
            return 'Game has not completed'


if __name__ == '__main__':
    solve()