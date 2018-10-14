# from collections import deque

# o, e, p

def cost_from_to(o, e, N):
    steps = e - o
    return N * steps - (steps * (steps-1)) / 2


def min_cost(N, M, trips):
    os = [o for o, e, p in trips]
    es = [e for o, e, p in trips]
    sorted_stations = sorted(list(set(os + es)))
    on_off = {}
    for o, e, p in trips:
        n_on, n_off = on_off.setdefault(o, (0, 0))
        on_off[o] = (n_on+p, n_off)
        n_on, n_off = on_off.setdefault(e, (0, 0))
        on_off[e] = (n_on, n_off+p)
    tickets = []
    cost = 0
    for i, s in enumerate(sorted_stations):
        n_on, n_off = on_off[s]
        tickets.append((n_on, s))
        while n_off > 0:
            n_tickets, origin_station = tickets.pop()
            n_used = min(n_off, n_tickets)
            cost += n_used * cost_from_to(origin_station, s, N)
            tickets_left = n_tickets - n_used
            n_off -= n_used
            if tickets_left:
                tickets.append((tickets_left, origin_station))
    return cost


def norm_cost(N, M, trips):
    cost = 0
    for o, e, p in trips:
        cost += p * cost_from_to(o, e, N)
    return cost


def solve(N, M, trips):
    return (norm_cost(N, M, trips) - min_cost(N, M, trips)) % 1000002013



##############################################################################

def read_ints(f):
    s = f.readline()
    return [int(w) for w in s.strip().split()]


from sys import argv

in_fn = argv[1]
out_fn = len(argv) > 2 and argv[2] or in_fn + '.out'

in_f = open(in_fn)
out_f = open(out_fn, 'w')

T = int(in_f.readline().strip())

for i_t in range(T):
    N, M = read_ints(in_f)
    trips = []
    for i in range(M):
        trip = read_ints(in_f)
        trips.append(trip)
    # cache = {}
    res = solve(N, M, trips)
    out_ln =  'Case #%d: %s' % (i_t+1, res)
    print >> out_f, out_ln
    print out_ln



