#!/usr/bin/python
import sys

def result(r):
    x_won = checkWon(r, 'X')
    o_won = checkWon(r, 'O')
    #print x_won
    #print o_won

    if x_won and o_won:
        return "Draw"
    if x_won:
        return "X won"
    if o_won:
        return "O won"
    if r.find('.') != -1:
        return "Game has not completed"
    return "Draw"


def checkWon(st, c):
    for i in range(4):
        br = False
        for j in range(4):
            if st[i*4 + j] == c or st[i*4 + j] == 'T':
                continue
            br = True
        if br == False: return True

    for i in range(4):
        br = False
        for j in range(4):
            if st[j*4 + i] == c or st[j*4 + i] == 'T':
                continue
            br = True
        if br == False: return True
                
    br = False
    for i in range(4):
        if st[i*4 + i] == c or st[i*4 + i] == 'T':
            continue
        br = True
    if br == False: return True

    br = False
    for i in range(4):
        if st[ (3-i)*4 + i] == c or st[(3-i)*4 + i] == 'T':
            continue
        br = True
    if br == False: return True
    return False

args = sys.argv
in_file = args[1]

f = open(in_file)

c = int(f.readline())

for cc in range(c):
    r = ''
    for i in range(4):
        r = r + f.readline()[:-1]
    #print r
    print "Case #" + str(cc+1) + ": " + result(r)
    #print 
    f.readline()

