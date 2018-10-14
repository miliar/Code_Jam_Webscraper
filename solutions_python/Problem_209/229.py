#!/usr/bin/python
import math

def solve(pancakes,k):
    ps = []
    for p in pancakes:
        params = p.split()
        r = int(params[0])
        h = int(params[1])
        ps.append((r,h))
    best = 0
    for i in range(len(ps)):
        bottom = ps[i]
        others = ps[:i] + ps[i+1:]
        others = [2 * p[0] * p[1] for p in others if p[0] <= bottom[0]]
        if len(others) >= k - 1 and k > 1:
            others.sort()
            heights = sum(others[- (k-1):])
            best = max(best, heights + 2 * bottom[0] * bottom[1] + bottom[0] ** 2)
        elif k == 1:
            best = max(best, 2 * bottom[0] * bottom[1] + bottom[0] ** 2)
    return math.pi * best

        



PATH = "/mnt/c/Users/mannes/Downloads/A-large (2).in"
#PATH = "test.in"
f = open(PATH, "r")
lines = f.readlines()

instances = [l.strip() for l in lines[1:]]
inum = 0

while instances:
    params = instances[0].split()
    n = int(params[0])
    k = int(params[1])
    pancakes = instances[1:1+n]
    instances = instances[1+n:]
    print "Case #{}: {}".format(inum + 1, solve(pancakes,k))
    inum += 1
