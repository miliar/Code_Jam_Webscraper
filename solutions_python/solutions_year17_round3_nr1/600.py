import math
from copy import deepcopy
from decimal import Decimal
import itertools
def pancakes_area(n, k, pancakes):
    cur_r = 0
    last_max_r = None
    cur_area = 0
##    print pancakes
    while len(pancakes) > n-k:
        area = map(lambda p: (p[0]>cur_r)*(p[0]**2-cur_r**2) + 
                   2*p[0]*p[1], pancakes)
        max_area_j = max(xrange(len(pancakes)), key=lambda j: area[j])
        cur_area += area[max_area_j]
##        print area[max_area_j]
##        print pancakes[max_area_j]
        if cur_r < pancakes[max_area_j][0]:
            cur_r = pancakes[max_area_j][0]
##            if last_max_r:
##                cur_area -= (2*last_max_r[0]*last_max_r[1])
##                pancakes.append(last_max_r)
##                last_max_r = pancakes[max_area_j]
        pancakes = pancakes[:max_area_j] + pancakes[max_area_j+1:]
##    print cur_area*math.pi
    return cur_area*math.pi

def pancakes_brute(n, k, pancakes):
    max_area = 0
    max_comb = None
##    print pancakes
    for c in itertools.combinations(xrange(n), k):
        max_r = max(map(lambda x: pancakes[x][0], c))
        area = sum(map(lambda x: 2*pancakes[x][0]*pancakes[x][1], c)) + \
                max_r**2
        if area > max_area:
            max_area = area
            max_comb = c
    print map(lambda x:pancakes[x], max_comb)
    print max_area*math.pi
    return max_area*math.pi
    
def main(fname):
    in_fd = open(fname, "rb")
    out_fd = open(fname + ".out", "wb")
    t = int(in_fd.readline().strip())
    for i in xrange(t):

        n, k = map(int, in_fd.readline().strip().split(" "))
        pancakes = []
        for j in xrange(n):
            pancakes.append(map(int, in_fd.readline().strip().split(" ")))

##        if i != 31:
##            continue
        ##        print "%d" % i, pancakes
        max_area = pancakes_area(n, k, pancakes)
        out_fd.write("Case #%d: %.9f\n" % (i+1, max_area))
    in_fd.close()
    out_fd.close()
