# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:25:19 2013

@author: soj
"""


# [[0 for x in xrange(4)] for x in xrange(4)]

def load_matrix(matrix, index, line):
    matrix.append(list(line))
    

def process_line(line):
    player_name = ''
    on_track = True
    for name in line:
        if (name == '.'):
            return None
        else:
            if(player_name != '' and name != 'T' and player_name != name):
                return None
            elif(name != 'T' and player_name == ''):
                player_name = name
    return player_name
        
    
def process_matrix(matrix, case):
    is_processed = False
    result = ''
    
    for row in matrix:
        name = process_line(row)
        if(name):
            result = "Case #" + str(case) + ": " + name + " won"
            is_processed = True
            break;

    xline = []
    yline = []
    idx = 3
    if(not is_processed):
        for i in xrange(4):
            column = []
            for j in xrange(4):
                column.append(matrix[j][i])
            
            name1 = process_line(column)
            if(name1):
                result = "Case #" + str(case) + ": " + name1 + " won"
                is_processed = True
                break;
            
            if(not is_processed):
                xline.append(matrix[i][i])
                yline.append(matrix[i][idx])
                idx -= 1
                
        if(not is_processed):
            name2 = process_line(xline)
            if(name2):
                result = "Case #" + str(case) + ": " + name2 + " won"
                is_processed = True
        
        if(not is_processed):
            name3 = process_line(yline)
            if(name3):
                result = "Case #" + str(case) +  ": " + name3 + " won"
                is_processed = True
   
    if(not is_processed):
        for i in xrange(4):
            if(not is_processed):
                for j in xrange(4):
                    if(matrix[i][j] == '.'):
                        result = "Case #" + str(case) + ": Game has not completed"
                        is_processed = True
                        break;
            else:
                break;

    if(not is_processed):
        result = "Case #" + str(case) + ": Draw"

    return result

number_of_test_cases = None
ins = open( "input.txt", "r" )

index = -1
matrix = []
case = 0
for l in ins:
    line = l.strip()
    if(number_of_test_cases is None):
        number_of_test_cases = int(line)
    else:
        if not line:
            index = -1
            matrix = []            
        else:
            index += 1
            load_matrix(matrix, index, line)
            if(index == 3):
                case += 1
                print process_matrix(matrix, case)
                
        
        if(case == number_of_test_cases):
            break;

            
    



