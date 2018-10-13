#!/usr/bin/env python

# Google code jam 2014

import sys

def result(i,mi,j,mj):
    row1 = mi[i-1]
    row2 = mj[j-1]

    dups = []

    for k in row1:
        if k in row2:
            dups.append(k)

    if len(dups) == 0:
        return 'Volunteer cheated!'
    elif len(dups) > 1:
        return 'Bad magician!'


    return str(dups[0])

def read_cards():
    m = []
    for i in range(4):
        m.append([0,0,0,0])
        line = sys.stdin.readline()
        for j in range(4):
            m[i][j],_,line = line.partition(' ')
            m[i][j] = int(m[i][j])
    return m

    
p = int(sys.stdin.readline())
for q in range(1,p+1):
    l = []

    i = int(sys.stdin.readline())
    mi = read_cards()

    j = int(sys.stdin.readline())
    mj = read_cards()

    print("Case #" + str(q) + ": " +  result(i, mi, j, mj))

