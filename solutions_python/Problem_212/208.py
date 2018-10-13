t = int(raw_input())
for case in xrange(1, t + 1):
    n, p = map(int, raw_input().split())
    groups = map(int, raw_input().split())
    buckets = [0 for _ in xrange(p)]
    for group in groups:
        buckets[group % p] += 1
    if p == 2:
        result = buckets[0] + (buckets[1] + 1) / 2
    elif p == 3:
        result = buckets[0]
        one_two = min(buckets[1], buckets[2])
        result += one_two
        buckets[1] -= one_two
        buckets[2] -= one_two
        result += (buckets[1] + buckets[2] + 2) / 3
    elif p == 4:
        result = buckets[0]
        result += (buckets[2] + 1) / 2
        one_three = min(buckets[1], buckets[3])
        result += one_three
        buckets[1] -= one_three
        buckets[3] -= one_three
        result += (buckets[1] + buckets[3] + 3) / 4
    else:
        result = -1
    print 'Case #%d: %d' % (case, result)
