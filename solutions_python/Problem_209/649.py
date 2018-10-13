from math import pi
from itertools import combinations

def area( pancake ):
    return pi * (pancake[0] ** 2)

def circumference( pancake ):
    return 2 * pi * pancake[0]

def arrange( pancakes ):
    pancakes = sorted( pancakes, reverse=True )
    exposed = 0

    for i in range( len(pancakes) - 1 ):
        exposed += pancakes[i][1] * circumference( pancakes[i] )
        exposed += area(pancakes[i]) - area(pancakes[i+1])

    exposed += area( pancakes[-1] ) + pancakes[-1][1] * circumference( pancakes[-1] )

    return exposed

for tc in range( 1, 1 + int( input() ) ):
    N, K = tuple( int(x) for x in input().split() )
    pancakes = []

    for n in range(N):
        pancakes.append( tuple( int(x) for x in input().split() ) )

    stacks = [list(x) for x in combinations(pancakes, K)]
    stacks = [ps for ps in map( arrange, stacks )]
    exposed = "%.9f" % max(stacks)
    print( "Case #{}: {}".format(tc, exposed) )
