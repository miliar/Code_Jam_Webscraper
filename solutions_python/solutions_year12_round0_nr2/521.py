import sys

input = sys.stdin
T = int(input.readline())
for t in xrange(T):
    line = [int(x) for x in input.readline().split()]
    N, S, p, gs = line[0], line[1], line[2], line[3:]
    count = 0
    for g in gs:
        d = p - 1 if p - 1 >= 0 else 0
        if (p + 2*d) <= g:
            count += 1
        else:
            d = p - 2 if p - 2 >= 0 else  0
            if (p + 2*d <= g and S > 0):
                count += 1
                S -= 1
    print "Case #%d: %d" % (t + 1, count)
