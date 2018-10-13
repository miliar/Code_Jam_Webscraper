import fractions


def solve(D, horses):
    time_till_arrival = 0

    for h in horses:
        t = fractions.Fraction(D - h[0], h[1])
        time_till_arrival = max(time_till_arrival, t)

    return D / time_till_arrival


T = int(raw_input())

for i in xrange(T):
    D, N = [int(x) for x in raw_input().split()]
    horses = []
    for j in xrange(N):
        horses.append([int(x) for x in raw_input().split()])

    print 'Case #%d: %0.6f' % (i + 1, solve(D, horses))
