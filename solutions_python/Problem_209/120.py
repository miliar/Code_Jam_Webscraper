import sys
from math import pi
def next_line():
    return input_file.readline().rstrip()

# Implicit pi factor
def cylinder((r, h)):
    return 2*r*h

input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    N, K = map(int, next_line().split())
    pancakes = []
    for i in range(N):
        pancakes.append(map(int, next_line().split()))
    pancakes.sort()
    #print pancakes, K, N, N-K, range(K-1, N)
    max_area = 0
    for i in xrange(K-1, N):
        sub = pancakes[:i]
        bottom = pancakes[i]
        sub.sort(key=lambda p: cylinder(p))
        cylinder_area = sum(cylinder(p) for p in sub[i-K+1:])
        area = cylinder_area + cylinder(bottom) + bottom[0]*bottom[0]
        #print i, area, sub, sub[i-K+1:], i-K+1, cylinder_area, cylinder(bottom), bottom[0]*bottom[0]
        max_area = max(max_area, area)
    #print max_area
    print max_area * pi
