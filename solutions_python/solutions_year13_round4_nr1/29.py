import sys


def cost(N, dist):
    return dist * N - (dist * (dist - 1)) / 2


def real_value(N, trips):
    total = 0
    for o, e, p in trips:
        total += p * cost(N, e - o)
    return total


def pay(N, tickets, s, p):
    x = tickets.keys()
    x = sorted(x)
    total = 0
    # print "pay at %s: %s" % (s, p)
    for i in xrange(len(x) - 1, -1, -1):
        o = x[i]
        # print "from:%s cost:%s count:%s" % (o, cost(N, s - o), tickets[o])
        if tickets[o] < p:
            total += tickets[o] * cost(N, s - o)
            p -= tickets[o]
            tickets.pop(o, None)
            # print total
        else:
            total += p * cost(N, s - o)
            tickets[o] -= p
            # print total
            return total
    raise Exception("Not enough tickets")


def compute(N, trips):
    expected = real_value(N, trips)
    stations = set()
    for o, e, p in trips:
        stations.add(o)
        stations.add(e)
    stations = sorted(list(stations))
    tickets = {}
    total = 0
    for s in stations:
        for o, e, p in trips:
            if o == s:
                if o in tickets:
                    tickets[o] += p
                else:
                    tickets[o] = p
        for o, e, p in trips:
            if e == s:
                total += pay(N, tickets, s, p)
    return "%s" % ((expected - total) % 1000002013)


def parse():
    N, M = map(int, sys.stdin.readline().strip().split())
    trips = []
    for i in xrange(M):
        o, e, p = map(int, sys.stdin.readline().strip().split())
        trips.append((o, e, p))
    return N, trips


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    count = 1
    part = 0
    if len(sys.argv) == 3:
        part = int(sys.argv[1])
        count = int(sys.argv[2])
    for i in xrange(T):
        data = parse()
        if i * count >= part * T and i * count < (part + 1) * T:
            result = compute(*data)
            print "Case #%d: %s" % (i + 1, result)
