T = int(raw_input())

for i in xrange(T):
    [D, N] = map(int, raw_input().split())
    horses = []
    for j in xrange(N):
        horses.append(tuple(map(float, raw_input().split())))

    time = []

    for (d, v) in horses:
        time.append((D-d) / v)

    t_max = max(time)

    print "Case #%d: %f" % ((i+1), D / t_max)
