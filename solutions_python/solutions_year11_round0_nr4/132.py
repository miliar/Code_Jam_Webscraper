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
def solve(N,C):
    return sum([C[i] != i+1 for i in range(0, len(C))])

""" DOIT """
T = int(lines.pop())
for CASE in range(1,T+1):
    N = int(lines.pop())
    C = [int(x) for x in lines.pop().split(' ')]
    result = solve(N,C)
    fout.write('Case #%s: %6f\n' % (CASE, result))
