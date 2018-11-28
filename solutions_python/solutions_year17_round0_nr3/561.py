t = int(raw_input())
for i in xrange(1, t + 1):
    n, m = [int(s) for s in raw_input().split(" ")]
    r = 1
    while r*2 <= m:
        r *= 2
    num = n - min(2*r-1, n)
    if num == 0:
        print "Case #{}: {} {}".format(i, 0, 0)
        continue
    base = num / r
    addi = num % r
    if addi > m - r:
        base += 1
    print "Case #{}: {} {}".format(i, (base + 1) / 2, base/2)
