#!/usr/bin/python2
""" INPUT """
import sys
input = sys.argv[1]
output = input.replace('in', 'out')
fin = open(input, 'r')
fout = open(output, 'w')
lines = [line.strip() for line in fin]
lines.reverse()

""" COMPUTE """
def solve(C, D, S):
    Cd = dict()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Dd = dict ((alpha[i], set()) for i in range(26))
    for a,b,c in C:
        Cd[(a,b)] = c
        Cd[(b,a)] = c
    for a,b in D:
        Dd[a].add(b)
        Dd[b].add(a)

    OUT = []
    for i in range(len(S)):
        OUT.append(S[i])
        while len(OUT) > 1:
            a,b = OUT[-1], OUT[-2]
            c = Cd.get((a,b), None)
            if c: # combine
                OUT.pop()
                OUT[-1] = c
                break
            else:
                if Dd[a].intersection(OUT):
                    OUT = []
            break
    return "[%s]" % ", ".join(OUT)

""" DOIT """
T = int(lines.pop())
for CASE in range(1,T+1):
    line = lines.pop().split(' ')
    line.reverse()

    c = int(line.pop())
    C = []
    for i in range (0,c):
        x = line.pop()
        C.append((x[0], x[1], x[2]))
    
    D = []
    d = int(line.pop())
    for i in range (0,d):
        x = line.pop()
        D.append((x[0], x[1]))

    N = int(line.pop())
    S = line.pop()

    result = solve(C, D, S)
    fout.write('Case #%s: %s\n' % (CASE, result))
