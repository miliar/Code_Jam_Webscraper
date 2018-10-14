import sys
import math


def getline():
    return sys.stdin.readline().strip()

getints = lambda: map(int, getline().split(' '))


mem = {}
def paint_cost(inner_r):
    inner_a = (inner_r ** 2)
    outer_a = ((inner_r + 1) ** 2)
    return outer_a - inner_a

cases, = getints()

for case in xrange(cases):
    r, t = getints()
    num_circles = 0
    # print r, t

    while True:
        t -= paint_cost(r)
        if t < 0:
            break
        r += 2
        num_circles += 1

    print "Case #{case}: {result}".format(case=case + 1, result=num_circles)
