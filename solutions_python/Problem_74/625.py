#!/usr/bin/env python

# Google code jam 2011 : Bot Trust

import sys

def other(c):
    if c == 'O':
        return 'B'
    else:
        return 'O'

def next_mov(p,bot):
    for el in p:
        if el[0] == bot:
            return el
    return

def result(p):
    time = 0
    pos = {
            "O" : 1,
            "B" : 1
            }

    while p != []:
        cur_bot = p[0][0]
        cur_dest = p[0][1]
        p = p[1:]
        delta = abs(cur_dest-pos[cur_bot])+1
        time += delta
        pos[cur_bot] = cur_dest

        # move the other bot
        nx_m = next_mov(p,other(cur_bot))
        if nx_m == None:
            continue

        if nx_m[1] >= pos[other(cur_bot)]:
            oth_dir = 1
        else:
            oth_dir = -1

        pos[other(cur_bot)] += min(delta,abs(pos[other(cur_bot)]-nx_m[1]))*oth_dir


    return time

p = int(sys.stdin.readline())
for s in range(1,p+1):
    line = sys.stdin.readline()
    n,_,line = line.partition(' ')
    n = int(n)
    p = []
    for i in range(n):
        r,_,line = line.partition(' ')
        pos,_,line = line.partition(' ')
        pos = int(pos)
        p.append([r,pos])

    print("Case #" + str(s) + ": " +  str(result(p)))

