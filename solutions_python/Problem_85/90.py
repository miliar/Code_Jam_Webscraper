import sys

def d_to_next(dists, star):
    c = len(dists)
    if star == 0:
        return dists[0]
    return dists[star % c]

def d_to_star(dists, star):
    t = 0
    for i in xrange(0, star):
        t += d_to_next(dists, i)
    return t

def total_dist(dists, n):
    d = 0
    for i in xrange(n):
        d += d_to_next(dists, i)
    return d

def dist_sped(dists, t, star):
    r = d_to_next(dists, star) - max(t/2 - d_to_star(dists, star), 0)
    return r

def solve(l, t, n, c, dists, casen):
    speedups = []
    for i in xrange(n):
        speedups.append(dist_sped(dists, t, i))
    speedups.sort()
    speedups = speedups[::-1]
    max_dist_sped = sum(speedups[:l])
    result = total_dist(dists, n)*2 - max_dist_sped
    print "Case #%d: %d" % (casen, result)

if __name__ == '__main__':
    with open(sys.argv[1], 'rU') as f:
        lines = f.readlines()
        ncases = int(lines[0])
        lines = lines[1:]
        for i in xrange(ncases):
            vals = map(int, lines[0].strip().split(' '))
            l, t, n, c = vals[:4]
            dists = vals[4:]
            solve(l, t, n, c, dists, i+1)
            lines = lines[1:]

