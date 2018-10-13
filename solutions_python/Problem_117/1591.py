# -*- coding: utf-8 -*-

import numpy as np
import pylab as pl
import math as m
#import decimal
#import sys
#from copy import copy, deepcopy


input_file = open('./input_file')
output_file = open('./output_file', 'w')

nbExp = int(input_file.readline().rstrip('\n'))

for k in np.arange(0,nbExp):
    (N, M) =  input_file.readline().rstrip('\n').split(' ')
    N = int(N)
    M = int(M)
    v = []
    
    for i in np.arange(0,N):
        v.append(input_file.readline().rstrip('\n').split(' '))
        
    for i in np.arange(0,N):
        for j in np.arange(0,M):
            v[i][j] = int(v[i][j])

    if (N <= 1 or M <= 1):
        output_file.write('Case #' + str(k+1) + ': YES\n')
    else:
        res = True # possible
        # for each square
        print v
        for i in np.arange(0,N):
            for j in np.arange(0,M):
                # tests if there is two different
                # direction in wich we can find
                # two grater (strictly) values
                # which implies an error
                resVer = True # verticaly possible
                resHor = True # horizontaly possible
                for i2 in np.arange(0,N):
                    if (v[i2][j] > v[i][j]):
                        resVer = False
                for j2 in np.arange(0,M):
                    if (v[i][j2] > v[i][j]):
                        resHor = False
                res = res and (resVer or resHor)
                if (res == False):
                    break
            if (res == False):
                break

        if (res):
            output_file.write('Case #' + str(k+1) + ': YES\n')
        else:
            output_file.write('Case #' + str(k+1) + ': NO\n')
                        


input_file.close()
output_file.close()

