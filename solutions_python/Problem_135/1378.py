#!/usr/bin/env pypy

T = int(raw_input())

def solution():
    solA = int(raw_input()) - 1
    a = []
    for i in range(4):
        a.append([int(x) for x in raw_input().split()])

    solB = int(raw_input()) - 1
    b = []
    for i in range(4):
        b.append([int(x) for x in raw_input().split()])

    intersect = set(a[solA]).intersection(set(b[solB]))
    if len(intersect) == 0:
        return "Volunteer cheated!"
    elif len(intersect) == 1:
        return list(intersect)[0]
    else:
        return "Bad magician!"

for i in range(T):
    print "Case #%s: %s" % (i+1, solution())

