import collections

def to_ints(s):
    return map(int, s.split())

def get_ints():
    return to_ints(raw_input())

n_cases = input()

def cost(n, a, b):
    d = abs(a-b)
    return (2*n*d+d*d+d)/2

for case in xrange(1, n_cases + 1):
    n_stops, n_pairs = get_ints()

    paths = []

    stops = collections.defaultdict(int)

    proper_total = 0

    for _ in xrange(n_pairs):
        begin, end, count = get_ints()
        stops[begin] += count
        stops[end] -= count
        proper_total += count * cost(n_stops, begin, end)

    total = 0

    paths.sort()
    stops = sorted(stops.iteritems())

    cur_tickets = []
    ind = 0

    for stop, diff in stops:
        while diff < 0:
            # preserve the longest tickets
            cheapest_tick = max(cur_tickets)
            removed = min(-diff, cheapest_tick[1])
            total += removed * cost(n_stops, cheapest_tick[0], stop)
            cheapest_tick[1] -= removed
            diff += removed
            cur_tickets = [t for t in cur_tickets if t[1]]
        if diff > 0:
            cur_tickets.append([stop, diff])

    total = (total - proper_total) % 1000002013

    print "Case #%d: %s" % (case, total)
