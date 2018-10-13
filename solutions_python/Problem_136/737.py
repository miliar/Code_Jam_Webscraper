import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    C, F, X = [float(x) for x in sys.stdin.readline().split()]
    A = [X / 2.0]
    B = [0]
    a = A[0]
    n = 1

    while True:
        B.append(B[n-1] + C / (2.0 + F * (n-1)))
        A.append(B[n] + X / (2.0 + F * n))
        if A[n] > a:
            break
        a = A[n]
        n += 1

    print "Case #%d: %f" % (t, a)
