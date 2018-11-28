#!/usr/local/bin/pypy
# run with PyPy 2.6.1

def read_strings():
    return raw_input().strip().split(' ')

def read_ints():
    return [int(x) for x in read_strings()]

class MaxMatching(object):
    def __init__(self, n, m):
        self.edges = [[] for i in xrange(n)]
        self.n = n
        self.m = m

    def add_edge(self, u, v):
        self.edges[u].append(v)

    def dfs(self, u):
        if self.t[u]:
            return False
        self.t[u] = True
        for v in self.edges[u]:
            if (self.q[v] == -1) or self.dfs(self.q[v]):
                self.q[v] = u
                return True
        return False

    def max_matching(self):
        self.q = [-1] * self.m
        self.t = [False] * self.n
        ans = 0
        for i in xrange(self.n):
            if self.dfs(i):
                ans += 1
                self.t = [False] * self.n
        return ans

def solve(a):
    m = len(a)
    mm = MaxMatching(m, m)
    for i in xrange(m):
        if a[i][1] == 1:
            for j in xrange(m):
                if a[j][1] == 2:
                    if a[i][0] != 1 or a[j][0] != 1:
                        mm.add_edge(i, j)
    matching_size = mm.max_matching()
    rides = m - matching_size
    mm = MaxMatching(m, m)
    for i in xrange(m):
        if a[i][1] == 1:
            for j in xrange(m):
                if a[j][1] == 2:
                    if (a[i][0] != a[j][0]) and (a[i][0] != 1 or a[j][0] != 1):
                        mm.add_edge(i, j)

    matching_size_zero_cost = mm.max_matching()
    return rides, matching_size - matching_size_zero_cost

# import random
# random.seed(123)
# for i in xrange(1000):
#     print random.randrange(1, 3), random.randrange(1, 3)

test_count, = read_ints()
for test in xrange(1, test_count + 1):
    n, c, m = read_ints()
    a = [0] * m
    for i in xrange(m):
        a[i] = read_ints()

    y, z = solve(a)
    print 'Case #{}: {} {}'.format(test, y, z)
