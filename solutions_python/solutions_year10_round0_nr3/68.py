#!/usr/bin/env python

import sys
fin = sys.stdin

def doIt(K, v, curPoz):
    aux = v[curPoz:] + v[:curPoz]

    SUM = 0
    steps = 0
    while SUM + aux[0] <= K and steps + 1 <= len(v):
        SUM += aux[0]
        aux = aux[1:] + [aux[0]]
        curPoz = (curPoz + 1) % len(v)
        steps += 1
    return SUM, curPoz

def main():
    T = int(fin.readline())
    for t in xrange(T):
        R, K, N = map(int, fin.readline().split())
        v = map(int, fin.readline().split())
        assert len(v) == N

        curPoz = 0
        seen = set()

        did = [-1 for i in range(N)]
        nxt = [-1 for i in range(N)]

        while curPoz not in seen:
            seen.add(curPoz)
            did[curPoz], nxt[curPoz] = doIt(K, v, curPoz)
            curPoz = nxt[curPoz]

        beginCycle = curPoz
        curPoz = 0
        SUM = 0
        while curPoz != beginCycle and R > 0:
            SUM += did[curPoz]
            curPoz = nxt[curPoz]
            R -= 1

        sumCycle = did[curPoz]
        lenCycle = 1
        curPoz = nxt[curPoz]
        while curPoz != beginCycle:
            sumCycle += did[curPoz]
            lenCycle += 1
            curPoz = nxt[curPoz]

        SUM += sumCycle * (R / lenCycle)
        R = R % lenCycle
        curPoz = beginCycle
        while R > 0:
            SUM += did[curPoz]
            curPoz = nxt[curPoz]
            R -= 1
        print "Case #%d: %d" % (t + 1, SUM)

    return 0

if __name__ == "__main__":
    main()

