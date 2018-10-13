import sys
import math


def eatMoveTimes(pan):
    if pan in [1,2,3]:
        return [1,2,3][pan-1], 0

    sq = int(math.sqrt(pan))
    if sq * sq == pan:
        return sq, sq-1
    elif sq*(sq+1) >= pan:
        return sq, sq
    else:
        return sq+1, sq

def moveTimeWithEat(pan, eat):
    m = math.ceil(1.0 * pan /eat) -1
    return max(m, 0)

def totalTimes(pans, eat):
    ret = eat
    #print "eat=%d, move=%d" % (eat, move)
    for pan in pans:
        m = moveTimeWithEat(pan, eat)
     #   print "pan=%d move=%d" % (pan , move)
        ret = ret + m

    return ret

def run(idx):
    D = int(sys.stdin.readline())

    line = sys.stdin.readline()
    arr = line.split(' ')
    pans = [int(x) for x in arr]

    maxP = max(pans)
    eat, move = eatMoveTimes(maxP)
    ret = maxP
    for x in xrange(eat, maxP):
        tmp = totalTimes(pans, x)
        ret = min(tmp, ret)

    res = "Case #%d: %d" % (idx, ret)
    print res

T = int(sys.stdin.readline())
for i in xrange(1, T+1):
#    print "=========", i
    run(i)
