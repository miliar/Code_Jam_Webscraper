def to_t(hhmm):
    h, m = hhmm.split(':')
    return int(h) * 60 + int(m)

cases = int(raw_input())
for case in xrange(cases):

    T = int(raw_input())
    NA, NB = [int(s) for s in raw_input().split()]

    events = []
    for i in xrange(NA):
        dep, arr = raw_input().split()
        events.append((to_t(dep), -1, 0))
        events.append((to_t(arr)+T, 1, 1))

    for i in xrange(NB):
        dep, arr = raw_input().split()
        events.append((to_t(dep), -1, 1))
        events.append((to_t(arr)+T, 1, 0))

    # arrivals must come before departures at the same time
    events.sort(cmp=lambda x,y: cmp(x[0],y[0]) if x[0] != y[0] else cmp(-x[1],-y[1]) )

    need = [0, 0]
    curr = [0, 0]

    for t, op, loc in events:
        curr[loc] += op
        if curr[loc] < 0:
            curr[loc] += 1
            need[loc] += 1

    print 'Case #%d: %d %d' % (case+1, need[0], need[1])
