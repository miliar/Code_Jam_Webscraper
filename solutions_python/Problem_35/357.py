import sys
import numpy


def memoized(f):
    cache = {}
    def wrap(*args):
        result = cache.get(args)
        if not result:
            result = cache[args] = f(*args)
        return result
    return wrap


def name_sinks(array):
    sinks = {}
    rows = []
    for r in xrange(array.shape[0]):
        cols = []
        for c in xrange(array.shape[1]):
            id = array[r, c]
            if id not in sinks:
                sinks[id] = chr(ord('a') + len(sinks))
            cols.append(sinks[id])
        rows.append(' '.join(cols))
    return '\n'.join(rows)


@memoized
def neighbors(shape, x, y):
    ns = []
    if x > 0:
        ns.append((x - 1, y)) # north
    if y > 0:
        ns.append((x, y - 1)) # west
    if y < shape[1] - 1:
        ns.append((x, y + 1)) # east
    if x < shape[0] - 1:
        ns.append((x + 1, y)) # south
    return ns


def flow(elev, x, y):
    ns = neighbors(elev.shape, x, y)
    min_elevation = elev[x, y]
    min_neighbor = None
    for n in ns:
        if elev[n] < min_elevation:
            min_elevation = elev[n]
            min_neighbor = n
    return min_neighbor


def label(elev, sink, x, y):
    if sink[x, y] == 0:
        n = flow(elev, x, y)
        sink[x, y] = n and label(elev, sink, *n) or sink.max() + 1
    return sink[x, y]


def test_case(handle):
    def ints():
        return map(int, handle.next().strip().split())
    r, c = ints()
    elev = numpy.array([ints() for _ in xrange(r)], dtype='i')
    test = elev.copy()
    sink = numpy.zeros(elev.shape, dtype='i')
    while (sink == 0).any():
        test[numpy.where(sink != 0)] = 0
        coords = divmod(test.argmax(), c)
        label(elev, sink, *coords)
    return sink


def run(handle):
    n = int(handle.next().strip())
    for i in xrange(n):
        print 'Case #%d:\n%s' % (i+1, name_sinks(test_case(handle)))
        print >> sys.stderr, 'completed', i, 'of', n


if __name__ == '__main__':
    run(sys.stdin)
