'''
Created on 13.04.2013

@author: Alex
'''
def analyse(matrix):
    game_finished = True
    for i in range(0,4):
        sum_x = 0
        sum_o = 0
        for j in range(0,4):
            if matrix[i][j] == 'O':
                sum_o += 1  
            elif matrix[i][j] == 'X':
                sum_x += 1
            elif matrix[i][j] == 'T':
                sum_x += 1
                sum_o += 1
            else:
                game_finished = False
        if  sum_x == 4:
            return 'X won'
        elif sum_o == 4:
            return 'O won'
    
    for i in range(0,4):
        sum_x = 0
        sum_o = 0
        for j in range(0,4):
            if matrix[j][i] == 'O':
                sum_o += 1  
            elif matrix[j][i] == 'X':
                sum_x += 1
            elif matrix[j][i] == 'T':
                sum_x += 1
                sum_o += 1
        if  sum_x == 4:
            return 'X won'
        elif sum_o == 4:
            return 'O won'

    sum_x = 0
    sum_o = 0    
    for i in range(0,4):
        for j in range(0,4):
            if i == j:
                if matrix[j][i] == 'O':
                    sum_o += 1  
                elif matrix[j][i] == 'X':
                    sum_x += 1
                elif matrix[j][i] == 'T':
                    sum_x += 1
                    sum_o += 1
    if  sum_x == 4:
        return 'X won'
    elif sum_o == 4:
        return 'O won'
    
    sum_x = 0
    sum_o = 0    
    for i in range(0,4):
        for j in range(0,4):
            if i == 3-j:
                if matrix[j][i] == 'O':
                    sum_o += 1  
                elif matrix[j][i] == 'X':
                    sum_x += 1
                elif matrix[j][i] == 'T':
                    sum_x += 1
                    sum_o += 1
    if  sum_x == 4:
        return 'X won'
    elif sum_o == 4:
        return 'O won'
         
    if game_finished:
        return 'Draw'
    else:
        return 'Game has not completed'
    
if __name__ == '__main__':
    f = open('A-large.in', mode='r')
    g = open('A-large.out', mode='w')
    n = int(f.readline())
    for i in range(1,n+1):
        matrix = []
        for j in range(0,4):
            vector = []
            l = list(f.readline())
            for k in range(0,4):
                vector.append(l[k])
            matrix.append(vector)
        f.readline()
        g.write('Case #' + str(i) + ': ' + analyse(matrix) + '\n') 