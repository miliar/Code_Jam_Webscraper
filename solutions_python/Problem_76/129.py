#!/usr/bin/python2
""" INPUT """
import sys
input = sys.argv[1]
output = input.replace('in', 'out')
fin = open(input, 'r')
fout = open(output, 'w')
lines = [line.strip() for line in fin]
lines.reverse()


def xor(l):
    return reduce(lambda x,y: x^y, l, 0)


""" COMPUTE """
def solve(N,C):
    if 0 == sum(C):
        return None
    if xor(C) != 0:
        return None
    return sum(C) - min(C)

""" DOIT """
T = int(lines.pop())
for CASE in range(1,T+1):
    N = int(lines.pop())
    C = [int(x) for x in lines.pop().split(' ')]
    result = solve(N,C)
    if result is None:
        result = "NO"
    fout.write('Case #%s: %s\n' % (CASE, result))
