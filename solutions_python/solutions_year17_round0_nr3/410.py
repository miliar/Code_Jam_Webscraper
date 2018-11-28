import sys

t = int(sys.stdin.readline().strip())

for tt in xrange(t):
    n, k = [int(i) for i in sys.stdin.readline().strip().split()]

    p = 0
    while ((p + 1) * 2 - 1 < k):
        p = (p + 1) * 2 - 1

    minimum = (n - p) // (p + 1)
    maximum_count = (n - p) - minimum * (p + 1)
    maximum = minimum + (1 if (maximum_count > 0) else 0)

    c = minimum if (maximum_count < k - p) else maximum

    print "Case #%d:" % (tt + 1), c - 1 - ((c - 1) // 2), (c - 1) // 2

