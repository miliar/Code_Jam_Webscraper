a = open('A-large.in')
cases = int(a.readline().strip())
for case in range(1, cases + 1):
    n, k = map(int, a.readline().strip().split(' '))
    k %= 2 ** n
    r = k == (2 ** n) - 1
    if r:
        r = 'ON'
    else:
        r = 'OFF'
    print 'Case #%d: %s' % (case, r)
a.close()