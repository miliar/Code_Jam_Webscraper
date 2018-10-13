from sys import argv
from itertools import *

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def read(inp):
    return inp.readline().split('\n')[0]

inp = open(argv[1])
T = int(read(inp))
for t in range(T):
    g = list(map(int, read(inp).split()))
    N = g[0]
    S = set(g[1:])
    subsets = powerset(S)
    subs_so_far = []
    s1 = set(next(subsets))
    done = False
    try:
        while not done:
            for s in subs_so_far:
                if sum(s1) == sum(s) and s.isdisjoint(s1) and \
                        s != set() and s1 != set():
                    done = True
                    break
            else:
                subs_so_far.append(s1)
                s1 = set(next(subsets))
        print("Case #%s:" % (t+1))
        print(*s1)
        print(*s)
    except StopIteration:
        print("Case #%s: Impossible" % (t+1))
