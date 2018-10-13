#! /usr/bin/env python

import sys
import os
import os.path

handle = open(sys.argv[1])

test_cases = []
mat = []
nb_test_cases = 0
index = -1
for line in handle:
    if index==-1:
        nb_test_cases=int(line)
    #print index
    if index>0:
        mat.append(line)
    if index==0:
        num = int(line)
        index = num+1
        if mat!=[]:
            test_cases.append(mat)
            mat = []
    
    index-=1
    if index==-2:
        index=0
if mat!=[]:
    test_cases.append(mat)
    mat = []

#print nb_test_cases
#print test_cases


wp = []
op_tab = []
owp = []
oowp = []
indice = 1
for case in test_cases:
    print 'Case #'+str(indice)+':'
    op_tab = []
    nb_games = []
    wp = []
    owp = []
    oowp = []
    for indiv in case:
        nb_win =0
        nb_game =0
        opponents = []
        index = 0
        for char in indiv:
            if char=='1':
                nb_win+=1
                nb_game+=1
            if char=='0':
                nb_game+=1
            if char=='0' or char=='1':
                opponents.append(index)
            index+=1
        op_tab.append(opponents)
        nb_games.append(nb_game)
        wp.append(nb_win/(1.0*nb_game))
    index =0
    for indiv in case:
        tmp = 0.0 #[]
        #print op_tab[index]
        for op in op_tab[index]:
            #print op
            bonus = 0
            if case[op][index]=='1':
                bonus = 1
            #print "you",op, wp[op], indiv[op]
            tmp +=(wp[op]*nb_games[op]-bonus)/(nb_games[op]-1.0)
        if len(op_tab[index])>0:
            owp.append(tmp/len(op_tab[index]))
        else:
            owp.append(0.0)
        index +=1
    index =0
    rpi = []
    for indiv in case:
        index2=0
        oowp_ = 0.0
        for op in op_tab[index]:
            oowp_ += owp[op]
            #print owp[op],op

        oowp.append(oowp_ /len(op_tab[index]))
        index +=1
    #print oowp
    index = 0
    for indiv in case:
        rpi.append(wp[index]*0.25+ owp[index]*0.5 + oowp[index]*0.25)
        index +=1
    for i in rpi:
        print i
    indice += 1
    #print owp

#print wp
