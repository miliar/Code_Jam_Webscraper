#!/usr/bin/env python
import sys
def solveCase(lines):
    v1 = int(lines[0]) - 1
    v2 = int(lines[5]) - 1
    r1 = map(int, lines[1 + v1].split())
    r2 = map(int, lines[6 + v2].split())
    p = [i in r1 and i in r2 for i in range(0,17)][1:]
    c = p.count(True)
    if c == 1:
        return p.index(True) + 1
    if c == 0:
        return "Volunteer cheated!"
    return "Bad magician!"

lines = [line.strip() for line in sys.stdin]
T = int(lines.pop(0))
assert len(lines) == T*10
for i in range(0, T):
    print "Case #{}: {}".format(i+1, solveCase(lines[0:10]))
    lines = lines[10:]
