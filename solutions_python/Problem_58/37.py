def check(A, B):
    if A > B:
        A, B = B, A

    if A == B:
        return False

    if B % A == 0:
        return True

    m = B / A
#    print m
    for i in xrange(m, 0, -1):
#        print i
        nB = B - i * A
#    print A, B, i, nB
        if not check(A, nB):
            return True
    return False

n_cases = int(raw_input())

for case in xrange(1, n_cases + 1):
    A1, A2, B1, B2 = map(int, raw_input().split())

    count = 0
    for A in xrange(A1, A2+1):
        for B in xrange(B1, B2+1):
            if check(A, B):
                count += 1

    print 'Case #%d: %d' % (case, count)

#for A in xrange(1, 40):
#    start = None
#    count = 0
#    B = 1
#    while True:
#        if not check(A, B):
#            if start is None:
#                start = B
#            count += 1
#        elif start is not None:
#            print A, start, count
#            break
#        B += 1
#
