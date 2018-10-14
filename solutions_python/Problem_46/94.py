import sys
fin = file(sys.argv[1], 'r')
T = int(fin.readline())

for t in xrange(1, T+1):
    n = int(fin.readline())
    rows = []
    for i in xrange(n):
        rows.append(fin.readline().rfind('1'))
    swaps = 0
    if n > 1:
        issorted = False
        while not issorted:
            issorted = True
            for i in xrange(n-1):
                if rows[i] > i:
                    issorted = False
                    break
            for j in xrange(i, n):
                if rows[j] <= i:
                    x = rows[j]
                    del rows[j]
                    rows.insert(i, x)
                    swaps += j - i
                    break
    print 'Case #%d: %d' % (t, swaps)
