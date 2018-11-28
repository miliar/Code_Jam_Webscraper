T = int(raw_input())
for test in xrange(T):
    tokens = [int(x) for x in raw_input().split(' ')]
    L = tokens[0]
    t = tokens[1]
    N = tokens[2]
    C = tokens[3]
    a = tokens[4:]
    half_t = t / 2
    answer = 0

    dists = []
    spans = []
    for i in xrange(N):
        spans.append(a[i % C])
        answer += 2 * spans[i]
        dists.append(spans[i])
        if i != 0: dists[i] += dists[i-1]

    boosters = []
    for l in xrange(L):
        gains = []
        for i in xrange(N):
            if i in boosters:
                gains.append(0)
            elif dists[i] <= half_t:
                gains.append(0)
            else:
                gains.append(min(dists[i] - half_t, spans[i]))
        max_gain = max(gains)
        #print gains, max_gain
        boosters.append(gains.index(max_gain))
        answer -= max_gain
    print "Case #%d: %d" % (test + 1, answer)

