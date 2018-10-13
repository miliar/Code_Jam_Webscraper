# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 07:00:45 2017

@author: Bert
"""

#flips K pancakes, does not change the order
#cannot flip fewer

#minimum number of uses of the OS PC F
#happy side up
#or IMPOSSIBLE
def inverse(c):
    if "+" == c:
        return "-"
    return "+"

def handle_case(cakes, k):
    
    #if all plusses
    if 0 == cakes.count("-"):
        return 0
    steps = 0
    
    cakes = list(cakes)
    while cakes.count("-") > 0:
        steps += 1
        loc = cakes.index("-")
        if loc+k > len(cakes):
            return "IMPOSSIBLE"
        for i in range(k):
            cakes[loc+i] = inverse(cakes[loc+i])
    return steps
    
#print (handle_case("---+-++-",3)) #3
#print (handle_case("+++++",4)) #0
#print (handle_case("-+-+-",4)) #impossible
#print (handle_case("-+-++",2)) #2
#print (handle_case("-++-",2)) #3
#print (handle_case("-+++--",3)) #3
#print (handle_case("--+++-",3)) #3
#print (handle_case("+--+--",3)) #2
#print (handle_case("---+---", 4)) #2
#print (handle_case("--++--+", 4)) #2

#with open("A-small.in") as fh, open("output-small.txt","w") as op:
with open("A-large.in") as fh, open("output-large.txt","w") as op:
        cases = int(fh.readline())
        x = 0
        for line in fh:
            x += 1
            cakes, k = line.split()
            o = "Case #{}: {}\n".format(x,handle_case(cakes, int(k)))
            print (o)
            op.write(o)