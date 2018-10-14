#!/usr/bin/env python

import sys

filename = sys.argv[1]
fin = open(filename, 'r')
T = int(fin.readline())

fout = open("output", 'w') 

for i in range(T):
    l = fin.readline().split()
    R = int(l[0])
    C = int(l[1])
    S = []
    for j in range(R):
        s = fin.readline()
        S.append(s)
    
    for j in range(R):
        result = True
        for k in range(C):
            if S[j][k]=='#':
                if (j==R-1)or(k==C-1)or(S[j][k+1]!='#')or(S[j+1][k]!='#')or(S[j+1][k+1]!='#'):
                    result = False
                    break;
                S[j]= S[j][:k]+'/'+S[j][k+1:]
                S[j]= S[j][:k+1]+'\\'+S[j][k+2:]
                S[j+1]= S[j+1][:k]+'\\'+S[j+1][k+1:]
                S[j+1]= S[j+1][:k+1]+'/'+S[j+1][k+2:]
        if not(result):
            break

    if not(result):
        fout.write("Case #" + str(i+1) + ":\nImpossible\n")
    else:
        fout.write("Case #" + str(i+1) + ":\n")
        for j in range(R):
            fout.write(S[j])


