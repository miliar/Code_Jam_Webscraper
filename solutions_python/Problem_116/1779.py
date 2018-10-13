# -*- coding: utf-8 -*-

import numpy as np
import pylab as pl
import math as m
#import decimal
#import sys

input_file = open('./input_file')
lines = []
for line in input_file:
    lines.append(line)
output_file = open('./output_file', 'w')

i = 0 # index of the current line
gameNbChar = []
gameNb = 0
for k in np.arange(0,len(lines[0])-1):
    gameNb += pow(10,len(lines[0])-2-k)*(int(lines[0][k]))

i += 1
caseNb = 0

while (caseNb < gameNb):
    #output_file.write("working on :\n"+lines[i]+lines[i+1]+lines[i+2]+lines[i+3])
    v = [] # memorize a special game
    
    result = False
    winner = 'Draw'
    complet = 'complet'

    for i1 in np.arange(0,4):
        for j in np.arange(0,4):
            if (lines[i+i1][j]=='.'):
                complet = 'Game has not completed'
                
    # Someone won in line
    for i2 in np.arange(0,4):
        if ((lines[i+i2][0] == 'T' or lines[i+i2][0] == 'X')
            and (lines[i+i2][1] == 'T' or lines[i+i2][1] == 'X')
            and (lines[i+i2][2] == 'T' or lines[i+i2][2] == 'X')
            and (lines[i+i2][3] == 'T' or lines[i+i2][3] == 'X')):
            winner = 'X won'
        if ((lines[i+i2][0] == 'O' or lines[i+i2][0] == 'T')
            and (lines[i+i2][1] == 'O' or lines[i+i2][1] == 'T')
            and (lines[i+i2][2] == 'O' or lines[i+i2][2] == 'T')
            and (lines[i+i2][3] == 'O' or lines[i+i2][3] == 'T')):
            winner = 'O won'

    # Someone won in column
    for j in np.arange(0,4):
        if ((lines[i][j] == 'T' or lines[i][j] == 'X')
                and (lines[i+1][j] == 'T' or lines[i+1][j] == 'X')
                and (lines[i+2][j] == 'T' or lines[i+2][j] == 'X')
                and (lines[i+3][j] == 'T' or lines[i+3][j] == 'X')):
            winner = 'X won'
        if ((lines[i][j] == 'O' or lines[i][j] == 'T')
                and (lines[i+1][j] == 'O' or lines[i+1][j] == 'T')
                and (lines[i+2][j] == 'O' or lines[i+2][j] == 'T')
                and (lines[i+3][j] == 'O' or lines[i+3][j] == 'T')):
            winner = 'O won'

    # first diag
    if ((lines[i][0] == 'T' or lines[i][0] == 'X')
        and (lines[i+1][1] == 'T' or lines[i+1][1] == 'X')
        and (lines[i+2][2] == 'T' or lines[i+2][2] == 'X')
        and (lines[i+3][3] == 'T' or lines[i+3][3] == 'X')):
        winner = 'X won'
    if ((lines[i][0] == 'T' or lines[i][0] == 'O')
        and (lines[i+1][1] == 'T' or lines[i+1][1] == 'O')
        and (lines[i+2][2] == 'T' or lines[i+2][2] == 'O')
        and (lines[i+3][3] == 'T' or lines[i+3][3] == 'O')):
        winner = 'O won'

    # second diag
    if ((lines[i][3] == 'T' or lines[i][3] == 'X')
        and (lines[i+1][2] == 'T' or lines[i+1][2] == 'X')
        and (lines[i+2][1] == 'T' or lines[i+2][1] == 'X')
        and (lines[i+3][2] == 'T' or lines[i+3][0] == 'X')):
        winner = 'X won'
    if ((lines[i][3] == 'T' or lines[i][3] == 'O')
        and (lines[i+1][2] == 'T' or lines[i+1][2] == 'O')
        and (lines[i+2][1] == 'T' or lines[i+2][1] == 'O')
        and (lines[i+3][0] == 'T' or lines[i+3][0] == 'O')):
        winner = 'O won'

        
    if (winner == 'Draw' and complet == 'Game has not completed'):
        output_file.write('Case #' + str(caseNb+1) + ': ' + 'Game has not completed' + '\n')
    else:
        output_file.write('Case #' + str(caseNb+1) + ': ' + winner + '\n')
        
    i += 5
    caseNb += 1
    
input_file.close()
output_file.close()
