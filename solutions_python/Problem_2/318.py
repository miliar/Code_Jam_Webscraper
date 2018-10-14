#! /usr/bin/env python
import sys
import heapq

class Case(object):
    def __init__(self, t, ab, ba):
        self.t = t
        self.ab = ab
        self.ba = ba

    @classmethod
    def read(self, read):
        t = int(read())
        na, nb = map(int, read().split())

        def parse_times(ln):
            def parse_time(tm):
                h, m = tm.split(':')
                return int(h) * 60 + int(m)
            return tuple(parse_time(tm) for tm in ln.split())
        ab = [parse_times(read()) for i in xrange(na)]
        ba = [parse_times(read()) for i in xrange(nb)]
        return self(t, ab, ba)

    def solve(self):
        t = self.t
        deltas = []
        for dep, arv in self.ab:
            deltas.append((dep,     1, 0, -1))
            deltas.append((arv + t, 0, 1, +1))
        for dep, arv in self.ba:
            deltas.append((dep,     1, 1, -1))
            deltas.append((arv + t, 0, 0, +1))
        deltas.sort()

        count = [0, 0]
        mins = [0, 0]
        for t, _, s, d in deltas:
            count[s] += d
            if count[s] < mins[s]:
                mins[s] = count[s]
        return -mins[0], -mins[1]

def main():
    read = raw_input
    for i in xrange(int(read())):
        print 'Case #%d: %d %d' % ((i + 1,) + Case.read(read).solve())

if __name__ == '__main__':
    main()
