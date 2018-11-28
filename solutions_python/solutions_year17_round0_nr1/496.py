#!/usr/bin/python

import sys

def flip( char ):
    if ( char == '-' ):
        return '+'
    else:
        return '-'

def isSad( char ):
    return ( char == '-' )

# Represent a stack of pancakes
# can be made faster if represented as bytestring and flipped by xor etc
class Stack:

    pancakes = []
    height = 0
    flipperLength = 0

    # Init based on data string
    def __init__( stack, stringData ):

        data = stringData.split(' ')
        stack.pancakes = list(data[0])
        stack.height = len(stack.pancakes)
        stack.flipperLength = int(data[1])

    # Flip k pancakes starting at index in stack
    def flip( stack, index ):

        if ( index > stack.height - stack.flipperLength ):
            raise Exception("Out-of-bounds flipping")

        for i in range( stack.flipperLength ):
            stack.pancakes[index+i] = flip( stack.pancakes[index+i] )

        

    # Find the next place which needs flipping
    # doin it the in total the slow quadratic way!
    def findNext( stack ):
        for i in range( stack.height ):
            if ( isSad( stack.pancakes[i] ) ):
                return i
        raise Exception( "Is already happy!" )

    # Check that the entire stack is happy
    def checkHappy( stack ):
        for i in range( stack.height ):
            if ( isSad( stack.pancakes[i] ) ):
                return False
        return True

def solve( s ):

    try:

        stack = Stack(s)
        flips = 0

        while( not stack.checkHappy() ):

            nextSad = stack.findNext() 
            stack.flip( nextSad )
            flips += 1

        return flips

    except Exception as e:
        return 'IMPOSSIBLE'


    

testcases = int( sys.stdin.readline() )
data = [ x.strip() for x in sys.stdin.readlines() ]
for i in range( testcases ):
    print( "Case #{}: {}".format( i+1, solve(data[i])) )



