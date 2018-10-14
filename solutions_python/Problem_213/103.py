t = int(raw_input())
for case in xrange(1, t + 1):
    n, c, m = map(int, raw_input().split())
    customers = {}
    maxtickets = 0
    seats = [0 for _ in xrange(n)]
    for i in xrange(m):
        p, b = map(int, raw_input().split())
        p -= 1
        if b not in customers:
            customers[b] = 0
        customers[b] += 1
        maxtickets = max(maxtickets, customers[b])
        seats[p] += 1

    lbound = 0
    result = 0
    snapshot = 0
    snapshot_max = max(seats)
    while lbound != len(seats):
        seats_max = max(seats)
        if seats_max < snapshot_max:
            snapshot = result
            snapshot_max = seats_max
        if seats_max <= maxtickets:
            break

        maxv = 0
        maxi = -1
        for i, v in enumerate(seats[lbound:]):
            if v > maxv:
                maxv = v
                maxi = i
        if maxv <= maxtickets:
            break
        if maxi == lbound:
            lbound = maxi + 1
            continue

        minnew = 1 << 63
        minnewi = -1
        for i, v in enumerate(seats[:maxi]):
            if v <= minnew:
                minnew = v
                minnewi = i
        if maxv <= minnew + 1:
            lbound = maxi + 1
            continue

        seats[maxi] -= 1
        seats[minnewi] += 1
        result += 1
    print 'Case #%d: %d %d' % (case, max(snapshot_max, maxtickets), result)
