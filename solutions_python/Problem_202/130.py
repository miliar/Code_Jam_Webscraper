#!/usr/bin/env python3


import numpy as np


def myprint(vis):
    for i in range(vis.shape[0]):
        out = ''
        for j in range(vis.shape[1]):
            out += vis[i,j]
        print(out)


def isvalid(s, r, c, oc, xc, pc):
    if s == '+':
        if (r, c) in pc:
            return False # there is already an +
        if r+c in [ri+ci for (ri, ci) in pc+oc]:
            return False # there is already an + or o in the same diagonal
        if r-c in [ri-ci for (ri, ci) in pc+oc]:
            return False # there is already an + or o the same diagonal
    elif s == 'x':
        if (r, c) in xc:
            return False # there is already an x
        if r in [ri for (ri, ci) in xc+oc]:
            return False # there is already an x or o in the same row
        if c in [ci for (ri, ci) in xc+oc]:
            return False # there is already an x or o in the same column
    elif s == 'o':
        if (r, c) in oc:
            return False # there is already an o
        if r in [ri for (ri, ci) in xc+oc] and not (r,c) in xc:
            return False # there is already an x in the same row which is not at the same position
        if c in [ci for (ri, ci) in xc+oc] and not (r,c) in xc:
            return False # there is already an x in the same column which is not at the same position
        if r+c in [ri+ci for (ri, ci) in pc+oc] and not (r,c) in pc:
            return False # there is already an x in the same diagonal which is not at the same position
        if r-c in [ri-ci for (ri, ci) in pc+oc] and not (r,c) in pc:
            return False # there is already an x in the same diagonal which is not at the same position
    else:
        raise Exception('This should not happen!')
    return True


T = int(input())
for t in range(1,T+1):
    N, M = map(int, input().split())
    vis = np.array([['.']*N]*N)
    oc, xc, pc = list(), list(), list()
    for m in range(M):
        s, r, c = input().split()
        r, c = int(r), int(c)
        if   s == '+':   pc.append((r,c))
        elif s == 'x':   xc.append((r,c))
        elif s == 'o':   oc.append((r,c))
        else:            raise Exception('This should not happen!')
        vis[int(r)-1,int(c)-1] = s #d[s]

    #if t in [25,66,84]:
    #    myprint(vis)
    #print(oc, xc, pc)
    ocn, xcn, pcn = list(), list(), list()

    reverse = (1,N) in oc
    for r in range(1,N+1):
        for c in range(1,N+1):
            if reverse:
                 c = N - c + 1
            if r == 1 and isvalid('o', r, c, oc+ocn, xc+xcn, pc+pcn):
                 if   (r,c) in pc: pc.remove((r,c))
                 elif (r,c) in xc: xc.remove((r,c))
                 if c == N:        reverse = True
                 ocn.append((r,c))
                 vis[r-1,c-1] = 'o'
            elif (r == 1 or r == N) and isvalid('+', r, c, oc+ocn, xc+xcn, pc+pcn):
                 pcn.append((r,c))
                 vis[r-1,c-1] = '+'
            elif isvalid('x', r, c, oc+ocn, xc+xcn, pc+pcn):
                 xcn.append((r,c))
                 vis[r-1,c-1] = 'x'
    score = len(xc+xcn) + len(pc+pcn) + 2*len(oc+ocn)
    added = xcn+pcn+ocn
    symbs = ['x']*len(xcn) + ['+']*len(pcn) + ['o']*len(ocn)
    max_s = 3*N-2
    #if score != max_s and score != 2:
    #    print('Score:', score, max_s)
    print('Case #%d: %d %d'%(t, score, len(added)))
    for s, (r,c) in zip(symbs, added):
        print('%s %d %d'%(s, r, c))

    #if t in [25,66,84]:
    #    myprint(vis)
    #print(oc, xc, pc)
    #print('next')












