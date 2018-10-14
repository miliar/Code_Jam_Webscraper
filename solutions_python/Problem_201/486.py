def large(n, k):
    bucket = {}
    bucket[n] = 1
    i = n
    st = n
    while 1:
        if bucket[i] > 0:
            if k <= bucket[i]:
                n = i
                break
            else:
                k -= bucket[i]
                if i % 2 == 1:
                    bucket[i/2] = bucket.get(i/2, 0) + bucket[i]*2
                else:
                    bucket[i/2] = bucket.get(i/2, 0) + bucket[i]
                    bucket[i/2-1] = bucket.get(i/2-1, 0) + bucket[i]
            if i-1 in bucket:
                i -= 1
            else:
                i = st / 2
                st = i
    if n % 2 == 1:
        return n/2, n/2
    else:
        return n/2, n/2-1

for _ in xrange(input()):
    print "Case #%d:" % (_+1),
    n, k = map(int, raw_input().split())
    print "%d %d" % large(n, k)
