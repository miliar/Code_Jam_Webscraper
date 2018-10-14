import sys
import os

os.chdir("/Users/nolze/Desktop")

fi = open("input.txt", 'r')
sys.stdin = fi

fo = open("output.txt", 'w')
sys.stdout = fo

for cs in range(input()):
    pre = map(int, raw_input().split())
    q = map(int, raw_input().split())

    p = 0
    seats = pre[1]

    for t in range(pre[0]):
        r = 0
        i = 0
        while True:
            if((r + q[0] > seats) or (i == pre[2])):
                p = p + r
                break
            r = r + q[0]
            q.append(q.pop(0))
            i += 1
    print "Case #" + str(cs+1) + ": " + str(p)

