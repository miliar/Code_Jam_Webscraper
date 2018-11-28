import sys

T = int(sys.stdin.readline())

for i in xrange(T):
    A, B = sys.stdin.readline().strip().split()

    A = int(A)
    B = int(B)

    res = 0

    for n in range(A,B):
        strn = str(n)
        for k in xrange(len(strn)):
            m = int(strn[k:] + strn[:k])
            if A <= m <= B and n < m:
                res = res + 1

    print "Case #%d: %d" % (i+1, res)

