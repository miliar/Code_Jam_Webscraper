T = int(raw_input())

used = [False]*2000001
for z in xrange(1, T+1):
    res = 0
    A, B = map(int, raw_input().split())
    ndigits = len(str(A))
    d = 10**(ndigits-1)
    for i in xrange(A, B+1):
        used[i] = False

    for i in xrange(A, B+1):
        if not used[i]:
            t, k = i, 0
            while True:
                if t <= B:
                    used[t] = True
                if t >= A and t <= B:
                    k += 1
                t = d*(t%10) + t/10
             #   print i, t
                if t == i:
                    break
            res += k*(k-1)/2

    print "Case #%d:" % z, res