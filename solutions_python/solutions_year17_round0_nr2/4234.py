t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    while n > 0:
        x = n
        while x > 0:
            l = x%10
            x = x/10
            sl = x%10
            if l < sl:
                break
        if x == 0:
            print "Case #{}: {}".format(i, n)
            break
        n = n - 1
