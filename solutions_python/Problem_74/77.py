
def solve(rps):
    t = 0
    pos = {'O': (0, 1), 'B': (0, 1)}
    for bot, button in rps:
        last_t, last_p = pos[bot]
        arrival = last_t + abs(last_p - button)
        flip = max(arrival, t) + 1
        t = flip
        pos[bot] = (t, button)
    return t

T = int(raw_input())
for t in xrange(1, T+1):
    rps_list = raw_input().split()[1:]
    rps = ((rps_list[2*i], int(rps_list[2*i+1])) for i in xrange(len(rps_list)/2))
    solution = solve(rps)
        
    print "Case #%d: %d" % (t, solution)
