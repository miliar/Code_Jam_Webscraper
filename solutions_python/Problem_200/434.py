T = input()

for tt in range(1, T + 1):
    N = input()
    a = [int(num) for num in list(str(N))]
    n = len(a)
    while True:
        isBreak = True
        for i in xrange(1, n):
            if a[i] < a[i-1]:
                isBreak = False
                a[i-1] -= 1
                for j in xrange(i, n):
                    a[j] = 9
        if isBreak:
            break
    print 'Case #%d: %d' % (tt, int(''.join(str(num) for num in a)))


