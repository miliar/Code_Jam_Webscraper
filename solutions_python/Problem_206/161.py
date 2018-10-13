import sys
from fractions import Fraction

def next_line():
    return input_file.readline().rstrip()

debug = False
#debug = True
input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    D, N = map(int, next_line().split())
    horses = []
    for i in xrange(N):
        horses.append(map(int, next_line().split()))
    horses.sort()
    if debug and len(horses) > 1 and horses[0][1] > horses[1][1]:
        print horses
        print D
    ipos, ispeed = horses[0]
    t = Fraction(0)
    for pos, speed in horses[1:]:
        #print t, ipos, ispeed, pos, speed
        if speed >= ispeed:
            continue
        #dist = float(pos - ipos) / (ispeed - speed)
        tdiff = Fraction(pos - ipos, (ispeed - speed))
        if ipos + tdiff * ispeed > D:
            break
        t += tdiff
        #print tdiff, ipos, ipos + tdiff * ispeed
        if debug:
            print "Take over at time", t, "pos", ipos + tdiff * ispeed, "new speed", speed
        ipos = ipos + tdiff * ispeed
        # ipos + t * ispeed = pos + t * speed
        # t * (ispeed - speed) = pos - ipos
        ispeed = speed
    t += Fraction(D - ipos, ispeed)
    if debug and len(horses) > 1 and horses[0][1] > horses[1][1]:
        print "Final segment", Fraction(D - ipos, ispeed), "finish", t
    #print Fraction(D - ipos, ispeed), D, ipos, ispeed
    aspeed = Fraction(D, t)
    print "%.6f" % float(aspeed)
