with open('A-large.in') as test:
    for i in range(1, int(test.next()) + 1):
        n, k = [int(x) for x in test.next().split()]
        print 'Case #%d: %s' % (i, 'ON' if (k + 1) % 2 ** n == 0 else 'OFF')
