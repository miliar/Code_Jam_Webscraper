import sys


T = int(sys.stdin.readline())

for i in range(T):
    X, R, C = map(int, sys.stdin.readline().split())
    area = R*C
    if area % X != 0 or area < X:
        print "Case #%d: %s" % (i+1, "RICHARD")
        continue
    if X == 1 or X == 2:
        print "Case #%d: %s" % (i+1, "GABRIEL")
        continue
    if X == 3:
        if R == 1 or C == 1:
            print "Case #%d: %s" % (i+1, "RICHARD")
        else:
            print "Case #%d: %s" % (i+1, "GABRIEL")
        continue
    if X == 4:
        if R <= 2 or C <= 2:
            print "Case #%d: %s" % (i+1, "RICHARD")
        else:
            print "Case #%d: %s" % (i+1, "GABRIEL")
        continue
    assert False
