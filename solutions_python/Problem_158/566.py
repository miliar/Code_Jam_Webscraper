import sys
import math

f = open(sys.argv[1])
n = int(f.readline())

for t in xrange(1,n+1):
    s = f.readline().strip("\n").split(" ")
    x = int(s[0])
    r = int(s[1])
    c = int(s[2])
    if x > max(r,c):
        print "Case #%d: RICHARD" % (t)
        continue
    if x > 6:
        print "Case #%d: RICHARD" % (t)
        continue
    if x == 4 and min(r,c) <= 2:
        print "Case #%d: RICHARD" % (t)
        continue
    if math.floor(float(x+1) / 2.0) > min(r,c):
        print "Case #%d: RICHARD" % (t)
        continue
    if (r*c) % x != 0:
        print "Case #%d: RICHARD" % (t)
        continue
    print "Case #%d: GABRIEL" % (t)


        










