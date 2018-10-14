def case (speeds, positions, B, K, T):
    cost = 0
    for i in range(K):
        # find out how many swaps each chicken needs to get to the front
        swaps = []
        for i in range(len(speeds)):
            if speeds[i]*T < B-positions[i]:
                continue

            swaps.append([0, i])
            for j in range(i+1, len(speeds)):
                if speeds[i] > speeds[j]:
                    swaps[-1][0] += 1

        if not swaps:
            return 'IMPOSSIBLE'

        swap, chick = min(swaps)
        #print 'Taking chicken', (positions[chick], speeds[chick]),
        #print 'to the front with', swap, 'swaps'
        cost += swap
        del speeds[chick]
        del positions[chick]

    return cost

C = int(raw_input())
for c in range(1, C+1):
    N, K, B, T = map(int, raw_input().split())
    ps = map(int, raw_input().split())
    ss = map(int, raw_input().split())
    print 'Case #%i:' % c, case(ss, ps, B, K, T)
