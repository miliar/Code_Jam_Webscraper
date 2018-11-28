"""
For each empty stall S, they compute two values LS and RS,
    each of which is the number of empty stalls between S
    and the closest occupied stall to the left or right, respectively.
    Then they consider the set of stalls with the farthest closest neighbor,
    that is, those S for which min(LS, RS) is maximal.

    If there is only one such stall, they choose it;
        otherwise, they choose the one among those where max(LS, RS) is maximal.
        If there are still multiple tied stalls,
        they choose the leftmost stall among those.

X___X
"""
from Queue import PriorityQueue


class Space():

    def __init__(self, L, R):
        self.L = L
        self.R = R
        self.priority = L - R

    def __cmp__(self, other):
        return cmp((self.priority, self.L), (other.priority, other.L))

    def midpoint(self):
        d, m = divmod(self.R - self.L, 2)
        return self.R - d - m

    def split(self):
        mid = self.midpoint()
        return Space(self.L, mid), Space(mid, self.R)

    def __str__(self):
        return "Space(Priority=%d)" % (self.priority)


def handle(N, K, i):
    q = PriorityQueue()
    q.put(Space(0, N + 1))
    for _ in xrange(K):
        space = q.get()
        # m = space.midpoint()
        l, r = space.split()
        q.put(l)
        q.put(r)
    z, y = sorted([-l.priority - 1, -r.priority - 1])
    print "Case #%d: %d %d" % (i, y, z)
    return z, y


def test():
    tests = [
        [(4, 2), (1, 0)],
        [(5, 2), (1, 0)],
        [(6, 2), (1, 1)],
        [(1000, 1000), (0, 0)],
        [(1000, 1), (500, 499)]
    ]
    err = "error: y: %d != %d and/or z: %d != %d"
    for i, test in enumerate(tests):
        ((n, k), (expected_y, expected_z)) = test
        actual_z, actual_y = handle(n, k, i + 1)
        assert actual_y == expected_y and actual_z == expected_z, err % (
            actual_y, expected_y, actual_z, expected_z)


def print_q(q):
    occupied = set()
    while not q.empty():
        space = q.get()
        occupied.add(space.R)
        occupied.add(space.L)

    print sorted(occupied)


def real():
    T = int(raw_input())
    for i in xrange(T):
        n, k = map(int, raw_input().split())
        handle(n, k, i + 1)


if __name__ == "__main__":
    # test()
    real()
