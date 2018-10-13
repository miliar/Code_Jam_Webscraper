def  cruise_control():
    D, N = map(int, raw_input().strip().split())
    max_time, pair = 0, None
    horses = [[0, float("inf")]]
    for _ in xrange(N):
        K, S = map(int, raw_input().strip().split())
        horses.append([K, S])
    horses.sort()
    for i in reversed(xrange(N)):
        K, S = horses[i+1]
        if 1.0 * (D - horses[i+1][0]) / horses[i+1][1] > 1.0 * (D - horses[i][0]) / horses[i][1]:
            horses[i][1] = 1.0 * (D - horses[i][0]) * S / (D - K)
    return horses[0][1]

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, cruise_control())