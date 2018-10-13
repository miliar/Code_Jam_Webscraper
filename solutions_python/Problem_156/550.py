c = int(raw_input())

for cc in xrange(c):
    n = int(raw_input())
    cnt = map(int, raw_input().strip().split())

    best_time = max(cnt)
    for max_after_distribution in xrange(1, max(cnt)):
        time = 0
        for c in cnt:
            time += (c-1) / max_after_distribution
        time += max_after_distribution
        best_time = min(best_time, time)

    print 'Case #%d: %d' % (cc+1, best_time)
