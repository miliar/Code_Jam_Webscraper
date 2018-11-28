# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:19:44 2013

@author: soj
"""

def process_matrix(matrix, case, rows, columns):

    stat_matrix = [[0 for x in xrange(columns)] for x in xrange(rows)]     
    
    #print stat_matrix
    
    for i in xrange(rows):
        start = None
        temp_stat = []
        is_valid = True
        for j in xrange(columns):
            if(start is None):
                start = matrix[i][j]
                temp_stat.append(1)
            elif(matrix[i][j] > start):
                is_valid = False
                break;
            elif(matrix[i][j] == start):
                temp_stat.append(1)
            else:
                temp_stat.append(0)                
        
        if(is_valid):
            for k in xrange(columns):
                if(stat_matrix[i][k] is 0 and temp_stat[k] == 1):
                    stat_matrix[i][k] = 1

    #print stat_matrix

    for i in xrange(columns):
        start = None
        temp_stat = []
        is_valid = True
        for j in xrange(rows):
            if(start is None):
                start = matrix[j][i]
                temp_stat.append(1)
            elif(matrix[j][i] > start):
                is_valid = False
                break;
            elif(matrix[j][i] == start):
                temp_stat.append(1)
            else:
                temp_stat.append(0)                
        
        if(is_valid):
            for k in xrange(rows):
                if(stat_matrix[k][i] is 0 and temp_stat[k] == 1):
                    stat_matrix[k][i] = 1            

    #print stat_matrix

    for i in xrange(columns):
        start = None
        temp_stat = []
        is_valid = True        
        for j in xrange(rows-1, -1, -1):
            if(start is None):
                start = matrix[j][i]
                temp_stat.append(1)
            elif(matrix[j][i] > start):
                is_valid = False
                break;
            elif(matrix[j][i] == start):
                temp_stat.append(1)
            else:
                temp_stat.append(0)                
        
        if(is_valid):
            for k in xrange(rows-1, -1, -1):
                if(stat_matrix[k][i] is 0 and temp_stat[(len(temp_stat) - 1) - k] == 1):
                    stat_matrix[k][i] = 1            

    #print stat_matrix
    
    for i in xrange(rows):
        start = None
        temp_stat = []
        is_valid = True        
        for j in xrange(columns-1, -1, -1):
            if(start is None):
                start = matrix[i][j]
                temp_stat.append(1)
            elif(matrix[i][j] > start):
                is_valid = False
                break;
            elif(matrix[i][j] == start):
                temp_stat.append(1)
            else:
                temp_stat.append(0)                
        
        if(is_valid):
            for k in xrange(columns-1, -1, -1):
                if(stat_matrix[i][k] is 0 and temp_stat[(len(temp_stat) - 1) - k] == 1):
                    stat_matrix[i][k] = 1            

    im_done = False
    for i in xrange(rows):
        im_done = False
        for j in xrange(columns):
            if( 0 == stat_matrix[i][j]):
                im_done = True
                print "Case #" + str(case) + ": NO"
                break;
        
        if(im_done):
            break;
            
    if(not im_done):
        print "Case #" + str(case) + ": YES"        

number_of_test_cases = None
ins = open( "input", "r" )
rows = None
columns = None
matrix = []
case = 0
num_of_rows=0
for l in ins:
    line = l.strip()
    if(number_of_test_cases is None):
        number_of_test_cases = int(line)
    elif(rows is None and columns is None):
        array = line.split(' ')
        rows = int(array[0])
        columns = int(array[1])
    else:
        num_of_rows += 1
        matrix.append(line.split(' '))
        
    if(num_of_rows == rows):
        case += 1        
        process_matrix(matrix, case, rows, columns)
        matrix = []
        rows = None
        columns = None
        num_of_rows=0

    if(case == number_of_test_cases):
        break;

