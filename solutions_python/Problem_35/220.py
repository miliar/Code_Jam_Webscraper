#!/usr/bin/env python

import sys

colors = {}
Forward = {}
letter = ord ("a")

def find_color (v):
    global colors, Forward, letter
    if (v in colors): return colors [v]
    if v not in Forward: # basin!
        colors [v] = chr (letter)
        letter += 1
    else:
        colors [v] = find_color (Forward [v])

    return colors[v]
    
def test ():
    global colors, Forward, letter
    h, w = map (int, sys.stdin.readline().split ())
    heights = {}
    for i in range(h):
        l = sys.stdin.readline().split()
        for j in range (w):
            heights [i,j] = l[j]

    # flow direction
    Forward = {}
    for i in range (h): 
        for j in range (w):
            eb = (i, j)
            for ty in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                try:
                    if (heights[ty] < heights[eb]): eb = ty 
                except KeyError, err:
                    pass
            if (heights[eb] < heights[(i,j)]):
                Forward [i,j] = eb

    colors = {}
    letter = ord ("a")
    for i in range (h):
        print reduce (lambda x,y: x + " " + y, [find_color((i,j)) for j in range (w)])


    
    
def main ():
    t = int (sys.stdin.readline())
    for i in range (t): 
        print "Case #" + str(i+1) + ":"
        test ()

main ()
