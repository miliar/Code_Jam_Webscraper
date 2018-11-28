file = "C-large.in"
import collections

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def split(i):
    return i / 2, (i - 1) / 2

def bathroom_stalls(N, K):
    """
    This turned out to answer the wrong question.
    """
    if not K:
        return N,

    Nmax, Nmin = split(N)
    Kmax, Kmin = split(K)

    subs = bathroom_stalls(Nmax, Kmax) + bathroom_stalls(Nmin, Kmin)
    return max(subs), min(subs)



def bathroom_stalls_2(N, K):
    counter = collections.Counter()
    counter[N] = 1

    if N == K:
        return 0, 0

    while True:
        n = max(counter)
        Nmax, Nmin = split(n)
        count = counter[n]

        if K <= count:
            return Nmax, Nmin

        del counter[n]
        counter[Nmax] += count
        counter[Nmin] += count
        K -= count



bathroom_stalls = Memoize(bathroom_stalls)

with open(file) as handle:
    T = int(handle.readline())

    for i in range(T):
        N, K = map(int, handle.readline().split(' '))

        # if bathroom_stalls(N, K) != bathroom_stalls_2(N, K):
        #     print N, K
        #     print bathroom_stalls(N, K)
        #     print bathroom_stalls_2(N, K)

        print 'Case #{}: {} {}'.format(i + 1, *bathroom_stalls_2(N, K))
