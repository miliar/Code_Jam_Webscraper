#!/bin/env python2
import sys

for i in range(5):
    if i>10:
        break
else:
    i=20

def do(S, t, ammount, canuse):
    while True:
        if t == len(S):
            if S[-1] != S[1]:
                return S
            else:
                back = goback( S, t, ammount, canuse )
                if back == None:
                    return None
                else:
                    S, t, ammount, canuse = back
                    continue
        last = S[t]
        for i in canuse[t]:
            if i != last:
                break
        else:
            i = None
        #
        if i == None:
            back = goback( S, t, ammount, canuse )
            if back == None:
                return None
            else:
                S, t, ammount, canuse = back
        else:
            S[t+1] = i
            

def solve2(N, R, O, Y, G, B, V):
    S = [None]*(N+1)
    ammount = [R, O, Y, G, B, V]
    return fmt( do( S, 0, ammount, [[ i for i in range(6) if ammount[i] ]] ) )


ammount=[2,0,2,0,2,0]
canuse = [ i for i in range(6) if ammount[i] ]

def solve(N, R, O, Y, G, B, V):
    s = [None]*N
    if max([R, O, Y, G, B, V]) * 2 > N:
        return "IMPOSSIBLE"
    a = zip( [R, O, Y, G, B, V], "ROYGBV" )
    a.sort()
    x, X = a.pop()
    y, Y = a.pop()
    z, Z = a.pop()
    #
    s[:2*x:2] = [X]*x
    #
    n = len( s[2*x-1::2] )
    s[2*x-1::2] = [Y]*n
    y -= n
    #
    n = len( s[2*x::2] )
    s[2*x::2] = [Z]*n
    z -= n
    #
    for i, j in enumerate(s):
        if j != None:
            continue
        if y >= z:
            s[i] = Y
            y -= 1
        else:
            s[i] = Z
            z -= 1
    return "".join(s)

def main():
    f = open( sys.argv[1] )
    T = int( f.next().strip() )
    for n in range(T):
        N, R, O, Y, G, B, V = map(int, f.next().strip().split())
        print "Case #{0}: {1}".format( n+1, solve(N, R, O, Y, G, B, V) )

main()

