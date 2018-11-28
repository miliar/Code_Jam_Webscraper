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
def solve(R,P):
    moves = {'O': 0, 'B': 0}
    last = {'O': 1, 'B': 1}
    other = {'O': 'B', 'B': 'O'}
    time = 0
    for i in range(0, len(R)):
        cur = R[i]
        t = 1 + max(0, abs(last[cur] - P[i]) - moves[cur])
        time += t
        last[cur] = P[i]
        moves[cur] = 0
        moves[other[cur]] += t
    return time

""" DOIT """
T = int(lines.pop())
for CASE in range(1,T+1):
    C = lines.pop().split(' ')
    R = [C[2*i+1] for i in range(0,len(C)/2)]
    P = [int(C[2*i+2]) for i in range(0,len(C)/2)]
    result = solve(R,P)
    fout.write('Case #%s: %s\n' % (CASE, result))
