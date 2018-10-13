import sys

def getnum():
    return [int(x) for x in sys.stdin.readline().split()]

T, = getnum()

for case in range(1, T + 1):
    R, k, N = getnum()
    G = getnum()

    off = [0 for x in range(N)] # -1?
    cost = [0 for x in range(N)] # -1?

    # find the cycle
    i = 0
    pos = 0

    hist = []

    while True:
        i += 1
        hist.append(pos)

        loaded = 0
        pos2 = pos
        off_v = 0

        if off[pos] == 0: # not yet visited
            while True:
                if loaded + G[pos2] > k or off_v == N: # no more space or no more people to take
                    cost[pos] = loaded
                    off[pos] = off_v
                    break

                off_v += 1
                loaded += G[pos2]
                pos2 += 1
                pos2 %= N
        else: # visited, its a cycle
            # find the cycle start and length
            for p in range(len(hist)):
                if hist[p] == pos:
                    cycle_start = p
                    cycle_length = (len(hist) - p - 1)
                    cycle_cost = sum([cost[x] for x in hist[p:-1]])

                    break
            break

        pos += off[pos]
        pos %= N

        # there is always a cycle of maximum length N
        if i == N+1: # no more rides today
            break

    prefix_cost = sum(cost[x] for x in hist[:p])
    if cycle_start + cycle_length >= R: # no full cycle has been completed
        cycle_cost = 0
        partial_cycle_cost = sum(cost[x] for x in hist[p:R])
    else:
        cycle_num = (R - cycle_start) / cycle_length
        cycle_cost *= cycle_num
        remainder = (R - cycle_start) % cycle_length
        partial_cycle_cost = sum([cost[x] for x in hist[p:p + remainder]])

    print "Case #%d: %d" % (case, prefix_cost + cycle_cost + partial_cycle_cost)
