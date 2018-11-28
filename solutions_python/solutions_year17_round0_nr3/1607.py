import heapq

class Solver_slow(object):
    def __init__(self, N, K):
        self.N = N
        self.K = K
        self.heap = []
        self._hpush(self.N)

    def _hpush(self, n):
        heapq.heappush(self.heap, -n)

    def _hpop(self):
        return -heapq.heappop(self.heap)

    def _min_and_max(self, n):
        return (n-1)//2, n//2

    def _add_person(self):
        interval = self._hpop()
        min_, max_ = self._min_and_max(interval)
        self._hpush(min_)
        self._hpush(max_)
        return min_, max_

    def run(self):
        for i in range(K-1):
            self._add_person()
        return self._add_person()


class Solver_fast(object):
    def __init__(self, N, K):
        self.N = N
        self.K = K

    def highest_2_power_lte(self, n):
        i = -1
        while n > 0:
            n = n >> 1
            i += 1
        return 1 << i

    def _min_and_max(self, n):
        return (n-1)//2, n//2

    def run(self):
        m = self.highest_2_power_lte(self.K)
        excess_splits = self.K - (m - 1)
        rem = (self.N - (m - 1)) % m
        num = 0
        quot = (self.N - (m-1)) // m
        if excess_splits <= rem:
            quot += 1
        return self._min_and_max(quot)

T = int(input())
for i in range(T):
    N, K = tuple(int(s) for s in input().split(' '))
    min_, max_ = Solver_fast(N, K).run()
    print('Case #%s: %s %s' % (i+1, max_, min_))
