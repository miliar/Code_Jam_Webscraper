def row(fn):
    return map(fn, raw_input().strip().split())

class City:
    def __init__(self, n):
        self.n = n
        self.E = self.S = 0
        self.D = {}

def calc_time(cities, n, e, s):
    try: length = cities[n].D[n+1]
    except KeyError: return 0.0
    time = length / float(s)
    if e < length: return float('+inf')
    e -= length
    nxt = cities[n+1]
    return time + min(calc_time(cities, n+1, e, s),
                      calc_time(cities, n+1, nxt.E, nxt.S))

for t in xrange(1, input()+1):
    N, Q = row(int)
    cities = {n: City(n) for n in xrange(1, N+1)}

    for n in xrange(1, N+1):
        city = cities[n]
        city.E, city.S = row(int)

    for n in xrange(1, N+1):
        city = cities[n]
        for j, d in enumerate(row(int), start=1):
            if d != -1:
                city.D[j] = d

    times = []
    for q in xrange(Q):
        U, V = row(int)
        city = cities[U]
        times.append(calc_time(cities, U, city.E, city.S))

    res = ' '.join('%f' % x for x in times)
    print 'Case #%d: %s' % (t, res)
