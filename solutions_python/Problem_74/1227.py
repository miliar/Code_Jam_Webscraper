#!/usr/bin/python

import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    p = f.readlines()
f.closed


num_tests = int(p[0])

tests = p[1:]

#for i in range(num_tests):
#    #print i
#    #print tests[i]
case = 0
totals = []

for i in tests:
    case += 1
    
    codes = i.split()
    ##print codes
    num_buttons = codes[0]
    bl = []
    o = []
    pairs = codes[1:]
    the_pairs = []
    ##print pairs
    for i in range(len(pairs)):
        if i % 2:
            continue
        if pairs[i] == 'B':
            bl.append(int(pairs[i+1]))
        if pairs[i] == 'O':
            o.append(int(pairs[i+1]))
        the_pairs.append((pairs[i], int(pairs[i+1])))
    #print "Case %d" % case
    #print "Orange"
    #print o
    #print "Blue"
    #print bl
    #print "starting the game"
    seconds = 1
    blue = 1
    orange = 1
    op = o[::-1]
    bp = bl[::-1]
    the_pairsp = the_pairs[::-1]
    while the_pairsp:
        #print "Second {0}, Blue {1}, Orange {2}".format(seconds, blue, orange)
        next_thing = the_pairsp[-1]
        if len(bp) == 0:
            pass
            #print "Blue Robot Done!"
            #print "Next thing is {0},  o is {1}".format(next_thing, op[-1])
        else:
            #blue decision tree
            if next_thing == ('B', blue):
                #print "blue Pressing Button"
                the_pairsp.pop()
                bp.pop()
            elif bp[-1] > blue:
                #print "blue Needs to walk forward"
                blue += 1
            elif bp[-1] < blue:
                #print "blue Needs to walk blackward"
                blue -= 1
        if len(op) == 0:
            #print "Orange Robot Done!"
            if len(bp) != 0:
                pass
                #print "Next thing is {0},  b is {1}".format(next_thing, bp[-1])
            else:
                pass
                #print "WhEEEE BEEES"
        else:
            #oj decision tree
            if next_thing == ('O', orange):
                #print "orange Pressing Button"
                the_pairsp.pop()
                op.pop()
            elif op[-1] > orange:
                #print "orange Needs to walk forward"
                orange += 1
            elif op[-1] < orange:
                #print "orange Needs to walk blackward"
                orange -= 1


        seconds += 1
        
    totals.append(seconds)

for i in range(len(totals)):
    print "Case #{0}: {1}".format(i+1,totals[i] - 1)

            

