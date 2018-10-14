#! /usr/bin/env python

import sys

# this program works with python version 2.3.4

if len(sys.argv) > 1 : file = open(sys.argv[1], "r")
else : file = sys.stdin

def getstr() : return file.readline().rstrip()

def getint() : return int(getstr())

def getfp() : return float(getstr())

def getarray() : return getstr().split()

def getintarray() : return [int(i) for i in getarray()]

def getfparray() : return [float(i) for i in getarray()]

def result(n,a) : print 'Case #' + str(n) + ':', a

T = getint()

for i in range(1, T + 1) :
    R, K, N = getintarray()
    grps = getintarray()
    rnds = [0 for j in range(0,N)]
    v = [-1 for j in range(0,N)]
    nr = 0
    g = 0
    ans = 0
    v[g] = 0
    while 1 :
        sum = 0
        while 1 :
            if sum + grps[g] > K : break
            sum += grps[g]
            g += 1
            if g == N :
                g = 0
                if not ans : break
        rnds[nr] = sum
        nr += 1
        ans += sum
        if v[g] != -1 or nr == R :
            break
        else :
            v[g] = nr
    rem = v[g]
    if rem == -1 :
        result(i, ans)
        continue
    loop = ans
    for j in range(0, rem) :
        loop -= rnds[j]
#    print 'Question', 'R', R, 'K', K
#    print grps
#    print rnds
#    print 'Answer', ans, 'loop', loop, 'nr', nr, 'g', g, 'Numloops', (R-nr)/(nr-rem), 'rem', rem, 'Remainder', (R-nr) % (nr-rem)
    ans += loop * ( ( R - nr ) / ( nr - rem ) )
    for j in range(0, ( R - nr ) % ( nr - rem )) :
        if rem == nr : rem = 0
#        print rnds[rem]
        ans += rnds[rem]
        rem += 1

    result(i, ans)

