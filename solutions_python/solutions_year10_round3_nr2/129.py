import math
for case in xrange(1, input() + 1):
    L, P, C = [float(x) for x in raw_input().split()]
    ans = math.ceil(math.log(math.log(P/L, C), 2))
    if ans < 0:
        ans = 0
    print 'Case #' + str(case) + ':', int(ans)
