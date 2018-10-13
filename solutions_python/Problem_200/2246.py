import os
import sys

def solve(l, i = 0, last = 0):
    if i == len(l):
        return True
    if int(l[i]) < last:
        return False
    while int(l[i]) >= last:
        if solve(l, i+1, int(l[i])):
            return True
        l[i] = str(int(l[i]) -1)
        l[i+1:] = ['9'] * (len(l)-i-1)
    return False




lines = open(sys.argv[1]).read().strip().split('\n')
for case, l in enumerate(lines[1:]):
    l = list(l)
    res = solve(l)
    print("Case #%d: %d" % (case+1, int("".join(l))))