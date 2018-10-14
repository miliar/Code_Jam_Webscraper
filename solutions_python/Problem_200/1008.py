T = input()
for _ in xrange(1, T + 1):
    n = [i for i in raw_input()]
    for i in range(1, len(n))[::-1]:
        if n[i - 1] > n[i]:
            n[i - 1] = str(int(n[i - 1]) - 1)
            for j in range(i, len(n)):
                n[j] = '9'
    n = ''.join(n)
    while n[0] == '0':
        n = n[1:]
    print 'Case #%d: %s' % (_, n)
