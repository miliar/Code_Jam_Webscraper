from math import sqrt
t = input()
for i in xrange(t):
    rings = 0
    r,t = map(int,raw_input().split())
    a = r
    qd = int(sqrt((2*r - 1)**2 + 8*t))
    rings = ((1 - 2*r) + qd)/4
    print "Case #" + str(i+1) + ": " + str(rings)
