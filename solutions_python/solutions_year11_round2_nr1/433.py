#!/usr/bin/env python

import sys

filename = sys.argv[1]
fin = open(filename, 'r')
T = int(fin.readline())

fout = open("output", 'w') 

for i in range(T):
    N = int(fin.readline())
    S = []
    W = [0.0 for ii in range(N)]
    G = [0.0 for ii in range(N)]
    WP = [0.0 for ii in range(N)]
    OWP = [0.0 for ii in range(N)]
    OOWP = [0.0 for ii in range(N)]    

    fout.write("Case #" + str(i+1) + ":\n")
    for j in range(N):
        s = fin.readline()
        S.append(s)
        for c in s:
            if c=='1':
                G[j]+=1
                W[j]+=1
            elif c=='0':
                G[j]+=1
        WP[j] = W[j]/G[j]

    for j in range(N):
        owp = 0.0
        for k in range(N):
            if (j!=k):
                if (S[j][k]=='1'):
                    owp += (W[k])/(G[k]-1)
                elif (S[j][k])=='0': 
                    owp += (W[k]-1)/(G[k]-1)
        OWP[j] = owp/G[j]

    for j in range(N):
        oowp = 0.0
        for k in range(N):
            if (j!=k)and(S[j][k]!='.'):
                oowp += OWP[k]
        OOWP[j] = oowp/G[j]

        Result = .25*WP[j] + .5*OWP[j] + .25*OOWP[j]
        fout.write(str(Result)+"\n")


