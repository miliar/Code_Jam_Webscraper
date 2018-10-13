#!/usr/bin/python

import re
import sys

input_file = sys.stdin


test_cases_num = int (input_file.readline ())

for case_num in xrange (1, test_cases_num + 1):
    first_line = input_file.readline ().split (' ')
    N = int (first_line[0])
    M = int (first_line[1])

    #print N 
    #print M
    possible = True

    matrix = []
    trough_matrix = []
    for i in xrange (0, N):
        matrix.append (\
            map ((lambda (x): int (x)), \
                 input_file.readline ().rstrip ('\n').split (' ')))
        trough_matrix.append ([False] * M)

    def flip_trough_hor (i, j1, j2):
        for j in xrange (j1, j2 + 1):
            trough_matrix[i][j] = True

    def flip_trough_hor_check (i, j1, j2, highest):
        for j in xrange (j1, j2 + 1):
            if (matrix[i][j] < highest):
                trough_matrix[i][j] = True

    def flip_trough_vert (j, i1, i2):
        for i in xrange (i1, i2 + 1):
            if (trough_matrix[i][j]):
                return True
        return False

    def flip_trough_vert_check (j, i1, i2, highest):
        for i in xrange (i1, i2 + 1):
            if (matrix[i][j] < highest and trough_matrix[i][j]):
                return True
        return False

        

    for i in xrange (0, N):
        highest = 0
        for j in xrange (0, M):
            #print ('highest = ' + str (highest))
            #print ('matrix[' + str (i) + '][' + str (j) + '] = ' + str(matrix[i][j]))
            if (matrix[i][j] > highest):
                highest = matrix[i][j]
        for j in xrange (0, M):
            if (matrix[i][j] < highest):
                trough_matrix[i][j] = True

    for j in xrange (0, M):
        highest = 0
        for i in xrange (0, N):
            #print ('highest = ' + str (highest))
            #print ('matrix[' + str (i) + '][' + str (j) + '] = ' + str(matrix[i][j]))
            if (matrix[i][j] > highest):
                highest = matrix[i][j]
        for i in xrange (0, N):
            if (matrix[i][j] < highest):
                if (trough_matrix[i][j]):
                    possible = False
                    break
            
        if (not possible):
            break

#    for j in xrange (0, M):
#        highest = 0
#        i1 = -1
#        began_trough = False
#        for i in xrange (0, N):
#            #print ('highest = ' + str (highest))
#            #print ('matrix[' + str (i) + '][' + str (j) + '] = ' + str(matrix[i][j]))
#            if (matrix[i][j] >= highest):
#                if (began_trough):
#                    began_trough = False
#                    if (flip_trough_vert (j, i1, i - 1)):
#                        possible = False
#                        break
#                elif (i != 0 and matrix[i][j] > highest):
#                    if (trough_matrix[i - 1][j]):
#                        possible = False
#                        break
#                highest = matrix[i][j]
#                    
#            elif (not began_trough):
#                i1 = i
#                began_trough = True 
#
#        if (not possible):
#            break
#
#        if (began_trough):
#            if (flip_trough_vert (j, i1, N - 1)):
#                possible = False
#                break


#    for j in xrange (0, M):
#        highest = 0
#        for i in xrange (0, N):
#            #print ('highest = ' + str (highest))
#            #print ('matrix[' + str (i) + '][' + str (j) + '] = ' + str(matrix[i][j]))
#            if (matrix[i][j] >= highest):
#                highest = matrix[i][j]
#            elif (trough_matrix[i][j]):
#                possible = False
#                break
#            #else:
#            #    trough_matrix[i][j] = True
#

                

    if (possible):
        print ('Case #' + str (case_num) + ': YES')
    else:
        print ('Case #' + str (case_num) + ': NO')

    #for x in matrix:
    #    print x 
    #for x in trough_matrix:
    #    print x 

    #for i in xrange (1, N + 1):



    

     
    


