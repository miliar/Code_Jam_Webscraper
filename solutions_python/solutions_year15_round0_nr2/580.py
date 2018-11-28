from math import ceil
import heapq

T = int( input() )
for Ti in range( 1, T+1 ):
    D = int( input() )
    P = [ int(i) for i in input().split() ]

    turns = 1000
    Pmax = max(P)
    for ni in range( 1, Pmax+1 ):
        si = 0
        for Pi in P:
            si += ( Pi-1 )//ni
        if ni+si < turns:
            turns = ni+si

    print( "Case #{0}: {1}".format( Ti, turns ) )

