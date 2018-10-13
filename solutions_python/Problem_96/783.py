import sys
import urllib2
import json
from time import sleep

fin = open( 'B-small-attempt0.in', 'r')
fout = open( 'b.out', 'w')

cases = fin.readline()
nList = []

for i in range( 0, 31):
    k = i / 3
    #print k
    if i % 3 == 0:
        nList.append( [k,k,k])
    elif i % 3 == 1:
        nList.append( [k,k,k+1])
    elif i % 3 == 2:
        nList.append( [k,k+1,k+1])

for i in range( int(cases)):
    line = fin.readline()
    para = line.split(' ')
    N = para[0]
    S = int(para[1])
    P = int(para[2])
    t = []
    r = []
    cnt = 0
    for j in range( 0, int(N)):
        t.append( nList[int(para[j+3])])
    
    for j in t:
        if j[2] >= P or j[1] >=P:
            cnt = cnt + 1
        elif j[2] == P-1 and j[2]-1 >= 0 and j[1]-1 >= 0 and j[1] ==P-1 and S > 0:
            cnt = cnt + 1
            S = S - 1
            if S == 0:
                break
    fout.write( "Case #" + str(i+1) + ": " + str(cnt) + '\n')
    
fout.close()
fin.close()

