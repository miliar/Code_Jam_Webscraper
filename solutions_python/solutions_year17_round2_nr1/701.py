f = open('A-large.in')
fw = open('A-large.out', 'w')

T = int(f.readline())
for t in xrange(T):
    D, N = map(int, f.readline().split())
    horses = []
    for n in xrange(N):
        K, S = map(int, f.readline().split())
        horses.append((K, S))
    horses.sort()

    max_time = 0
    for h in reversed(horses):
        time_ = 1.0 * (D - h[0]) / h[1]
        if time_ > max_time:
            max_time = time_
    fw.write('Case #' + str(t + 1) + ': ' + '{0:.10f}'.format(1.0 * D / max_time) + '\n')

fw.close()
f.close()
