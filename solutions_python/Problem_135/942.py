#!/usr/bin/python3

import sys

def case():
    a1 = int(sys.stdin.readline())
    p1 = []
    for i in range(4): p1.append([int(x) for x in sys.stdin.readline().split()])
    a2 = int(sys.stdin.readline())
    p2 = []
    for i in range(4): p2.append([int(x) for x in sys.stdin.readline().split()])

    l1 = p1[a1-1]
    l2 = p2[a2-1]
    a = []
    for x in l1:
        if x in l2: a.append(x)
    if len(a) == 1:
        return a[0]
    elif len(a) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

T = int(sys.stdin.readline())
for i in range(1,T+1):
    print("Case #%s: %s" % (i, case()))
    

