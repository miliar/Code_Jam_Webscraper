#!/usr/bin/pypy

import itertools

def cnts(S):
    cnt = 1
    bor = {}
    for s in S:
        cur = bor
        for x in s:
            if x in cur:
                cur = cur[x]
            else:
                cnt+=1
                cur[x] = cur = {}
    return cnt

def calc(S, ost, pcnt=0):
    if ost==1:
        global pmax, rcnt
        cnt = cnts(S)
        if cnt + pcnt > pmax:
            pmax = cnt + pcnt
            rcnt = 1
        elif cnt + pcnt == pmax:
            rcnt += 1
        return
    res = 0
    for i in range(1,len(S)-ost+2):
        for comb in itertools.combinations(S,i):
            l1 = comb
            l2 = [x for x in S if x not in l1]
            calc(l2,ost-1,pcnt+cnts(l1))

def solve():
    M, N = map(int,raw_input().split())
    S = [raw_input().strip() for _ in range(M)]
    global pmax, rcnt
    pmax = rcnt = 0
    calc(S, N)
    return "%d %d"%(pmax, rcnt)

if __name__ == "__main__":
    T = int(raw_input())
    for t in range(1,T+1):
        print "Case #%d:"%t,solve()
