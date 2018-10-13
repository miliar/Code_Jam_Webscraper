#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')

from collections import defaultdict

edges=["VY","YV","BO","OB","GR","RG",
       "YB","BY","RB","BR","RY","YR"]

def run(T):
    N, R, O, Y, G, B, V = map(int, input.readline().split())
    #if T!=6: return '--'
    save = [R, O, Y, G, B, V]
    #print save
    s = ""
    while True:
        #print R,O,Y,G,B,V
        #print "--", s
        if R == 0 and O == 0 and Y == 0 and G == 0 and B == 0 and V == 0:
            break
        if len(s) == 0:
            if Y >= R and Y >= B:
                Y -= 1
                s += 'Y'
            elif B >= Y and B >= R:
                B -= 1
                s += 'B'
            elif R:
                R -= 1
                s += 'R'
            else:
                return 'IMPOSSIBLE'
        else:
            c = s[-1]
            if c == 'V':
                Y -= 1
                s += 'Y'
            elif c == 'O':
                B -= 1
                s += 'B'
            elif c == 'G':
                R -= 1
                s += 'R'
            elif c == 'Y':
                if V > 0:
                    V -= 1
                    s += 'V'
                elif B-O >= R-G:
                    B -= 1
                    s += 'B'
                else:
                    R -= 1
                    s += 'R'
            elif c == 'B':
                if O > 0:
                    O -= 1
                    s += 'O'
                elif R-G >= Y-V:
                    R -= 1
                    s += 'R'
                else:
                    Y -= 1
                    s += 'Y'
            elif c == 'R':
                if G > 0:
                    G -= 1
                    s += 'G'
                elif Y-V >= B-0:
                    Y -= 1
                    s += 'Y'
                else:
                    B -= 1
                    s += 'B'
        if min([R, O, Y, G, B, V]) < 0:
            return 'IMPOSSIBLE'
        #print "++ ", s
    if (s[0] + s[-1]) in edges:
        for i in range(len(s)-1):
            assert s[i] + s[i+1] in edges
        return s
    else:
        if len(s) > 2:
            s = s[:-2] + s[-1] + s[-2]
            if (s[-3]+s[-2] in edges) and (s[-2]+s[-1] in edges) and (s[-1]+s[0] in edges):
                return s
        return 'IMPOSSIBLE'
            
            
T = int(input.readline())
for t in range(T):
    print >> output, 'Case #{}: {}'.format(t+1,run(t+1))
