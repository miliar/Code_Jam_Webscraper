#!/usr/bin/python
import sys

case = int(sys.stdin.readline())
for ca in range(case):
    row = int(sys.stdin.readline())
    origin = []
    for i in range(4):
        cur = sys.stdin.readline()
        if i+1 == row:
            origin = [int(x) for x in cur.split(' ')]
    
    row = int(sys.stdin.readline())
    changed = []
    for i in range(4):
        cur = sys.stdin.readline()
        if i+1 == row:
            changed = [int(x) for x in cur.split(' ')]

    same = 0
    ans = -1
    for i in origin:
        for j in changed:
            if i == j:
                same += 1
                ans = i

    if same == 1:
        print "Case #%d: %d" % ((ca+1), ans)
    elif same > 1:
        print "Case #%d: Bad magician!" % (ca+1)
    else:
        print "Case #%d: Volunteer cheated!" % (ca+1)

