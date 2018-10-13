from __future__ import division

def B((B, E, w)):
    return B

def E((B, E, w)):
    return E

def w((B, E, w)):
    return w

def L((B, E, w)):
    return E-B

def case():
    X, S, R, t, N = map(int, raw_input().split())
    walkways = [map(int, raw_input().split()) for i in xrange(N)]
    length = sum(L(walkway) for walkway in walkways)
    unway = X-length
    walkways.append((0, unway, 0))
    walkways.sort(key=w)

    times = []
    for walkway in walkways:
        run_time = min(t, L(walkway)/(w(walkway) + R))
        t -= run_time
        run_dist = run_time*(w(walkway)+R)
        walk_dist = L(walkway) - run_dist
        walk_time = walk_dist/(w(walkway) + S)
        """
        assert run_dist <= L(walkway), (run_dist, L(walkway))
        assert run_time >= 0, walkway
        assert run_dist >= 0, walkway
        assert walk_dist >= 0, (walkdist, walkway)
        assert walk_time >= 0, (walkway, walk_time)
        """
        times.append(run_time)
        times.append(walk_time)
    times.sort()
    return sum(times)

T = int(raw_input())
for i in xrange(1, T+1):
    print 'Case #%i: %0.7f' % (i, case())
