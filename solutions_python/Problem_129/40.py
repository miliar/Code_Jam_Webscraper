def cost(N, d):
    return (2 * N - d + 1) * d / 2

T = input()
for _ in xrange(T):
    before, events = 0, []
    [N, M] = map(int, raw_input().split())
    for i in xrange(M):
        [o, e, p] = map(int, raw_input().split())
        before += cost(N, e - o) * p
        events.append((o, -p))
        events.append((e, p))
    events.sort()

    after, passengers = 0, []
    for (v, p) in events:
        if p < 0:
            passengers.append((v, -p))
        else:
            while passengers[-1][1] < p:
                after += cost(N, v - passengers[-1][0]) * passengers[-1][1];
                p -= passengers[-1][1]
                passengers.pop()
            if p > 0:
                after += cost(N, v - passengers[-1][0]) * p
                tmp = (passengers[-1][0], passengers[-1][1] - p)
                passengers.pop()
                passengers.append(tmp)

    print "Case #%d: %d" % (_ + 1, before - after)
