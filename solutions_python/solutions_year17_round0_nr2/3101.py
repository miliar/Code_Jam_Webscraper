t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    base = len(s)
    n = int(s)
    res = 0

    for power in range(1, len(s)+1):
        last = (n % 10 ** power - n % 10 ** (power-1)) / 10 ** (power-1)
        but_last = ((n % 10 ** (power + 1) - n % 10 ** power) / 10 ** power)
        if power > len(str(n % 10 ** power)):
            last = 0
        if last < but_last:
            n -= (n % 10 ** power + 1)
    print "Case #{}: {}".format(i, n)