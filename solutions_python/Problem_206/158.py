tests = int(raw_input())

for test in xrange(tests):
    d, n = map(int, raw_input().split())
    max_time = 0
    for i in xrange(n):
        p, s = map(float, raw_input().split())
        if p >= d:
            continue
        max_time = max(max_time, (d - p)/s)
    res = d / max_time if max_time > 0 else 0
    print "Case #{}: {}".format(test+1, res)
