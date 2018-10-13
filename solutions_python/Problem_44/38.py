import sys
import math




def get_next_case(inp):
    T = int(inp.readline())
    for t in xrange(T):
        N = int(inp.readline())
        flies = []
        for n in xrange(N):
            flies.append(map(float, inp.readline().split()))
        yield flies


def get_m_func(flies):  # returns M(t), (x, v)
    N = len(flies)
    sums = []
    for i in xrange(len(flies[0])):
        sums.append(sum(fly[i] for fly in flies) / N)
    
    x0, y0, z0, vx, vy, vz = sums

    def M(t):
        return (x0 + t * vx, y0 + t * vy, z0 + t * vz)

    return (M, (x0, y0, z0, vx, vy, vz))


def sq_dist(coords):
    return math.sqrt(sum(coord ** 2 for coord in coords))


def main():
    assert len(sys.argv) == 3, "%s inpfile outpfile" % sys.argv[0]

    inp = open(sys.argv[1], 'rt')
    outp = open(sys.argv[2], 'wt')

    for n, flies in enumerate(get_next_case(inp)):
        M, vec = get_m_func(flies)
        x, y, z, vx, vy, vz = vec
        t1 = vx ** 2 + vy ** 2 + vz ** 2
        if t1 <= 0.0000001:
            t, d = 0, sq_dist(M(0))
        else:
            t = -(x * vx + y * vy + z * vz) / t1
            t = t if t > 0 else 0
            d = sq_dist(M(t))

        print d, t, vec
        outp.write('Case #%d: %.8f %.8f\n' % (n + 1, d, t))

    inp.close()
    outp.close()


if __name__ == '__main__':
    main()

