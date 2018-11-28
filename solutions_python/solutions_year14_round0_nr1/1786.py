#!/usr/bin/python
import sys

# Magic Trick

lines = [l.rstrip() for l in sys.stdin.readlines()]
for x in xrange(int(lines.pop(0))):
    ans1, ans2 = lines[10*x], lines[10*x+5]
    mat1, mat2 = [l.split() for l in lines[10*x+1:10*x+5]], [l.split() for l in lines[10*x+6:10*x+10]]
    row1, row2 = mat1[int(ans1)-1], mat2[int(ans2)-1]
    outcome = set(row1).intersection(row2)
    if len(outcome) == 1:
        result = list(outcome)[0]
    elif len(outcome) > 1:
        result = "Bad magician!"
    else:
        result = "Volunteer cheated!"
    print("Case #%u: %s" % (x + 1, result))
