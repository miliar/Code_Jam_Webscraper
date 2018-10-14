import math

def test(rank, left, right, n, x, y) :
    if n == 0 :
        if x > 0 :
            if right > y :
                return 1.0
            else :
                return 0.0
        else :
            if left > y :
                return 1.0
            else :
                return 0.0
    # left case
    leftres = 0
    if left < rank * 2 :
        leftres = test(rank, left + 1, right, n - 1, x, y)
    # right case
    rightres = 0
    if right < rank * 2 :
        rightres = test(rank, left, right + 1, n - 1, x, y)

    if left < rank * 2 :
        if right < rank * 2 :
            return leftres * 0.5 + rightres * 0.5
        else :
            return leftres
    else :
        return rightres

t = int(raw_input())
for casenum in range(1, t + 1) :
    n, x, y = [int(z) for z in raw_input().split()]
    if (x == 0) and (y == 0) :
        print "Case #%d: 1.0" % casenum
        continue

    rank = (abs(x) + y) / 2
    maxn = (2 * rank * rank) + (3 * rank ) + 1
    minn = (2 * rank - 1) * rank
    if n >= maxn :
        print "Case #%d: 1.0" % casenum
        continue
    elif y == rank * 2 :
        print "Case #%d: 0.0" % casenum
        continue
    elif n <= minn :
        print "Case #%d: 0.0" % casenum
    else :
        print "Case #%d: %F" % (casenum, test(rank, 0, 0, n - minn, x, y))
