import fileinput

import fractions
from fractions import Fraction
import itertools
from math import factorial
from collections import Counter


COLLECT_POSITION_COUNT = []

def build_collect_position_count(N):
    global COLLECT_POSITION_COUNT
    COLLECT_POSITION_COUNT = [ [1], [0,1] ]

    for n in xrange(2, N+1):
        n_1 = COLLECT_POSITION_COUNT[-1]
        n_2 = COLLECT_POSITION_COUNT[-2]
        count = [0] + n_1
        subcnt = n_1[:]
        for i in xrange(n-1):
            subcnt[i+1] -= n_2[i]
            subcnt[i] += n_2[i]
            count[i] += subcnt[i] * (n-1)
        COLLECT_POSITION_COUNT.append(count)



def count_collect_positions(seq):
    count = 0
    for i,n in enumerate(seq):
        if i==n: count += 1
    return count

_CACHE = [0,0,2,3] + [-1]*100

def calc_expect(n, indent=' '):
    if n < 100:
        cached = _CACHE[n]
        if cached >= 0:
            return cached

    exp = 0
    a = 0

    recurse_count = 0
    notrecurse_count = 0
    group_pat = group_pat_gen(n)

    for g in group_pat:
        combi = calc_group_c(n, g)
        if g == (n,):
            recurse_count = combi
        elif not g:
            notrecurse_count += 1
            exp += 1
        else:
            notrecurse_count += combi
            subexp = sum(calc_expect(m, indent+'  ') for m in g)
            exp += combi * (subexp+1)
    res = recursive_expected(
            recurse_count+notrecurse_count,
            recurse_count,
            Fraction(exp) / notrecurse_count)
    if n < 100:
        _CACHE[n] = res
    return res

def recursive_expected(base, recursive_ratio, norecurse_expect):
    return norecurse_expect + fractions.Fraction(recursive_ratio) / (base-recursive_ratio)

def build_min_expect_dp(N):
    global EXPECTS
    EXPECTS = [0,0]
    for n in xrange(2, N+1):
        # n unsorted integers.
        #base = factorial(n)
        expects = []
        for m in xrange(1):
            # hold m
            print n, "unsorted, holds", m
            ecpc = COLLECT_POSITION_COUNT[n-m]
            base = sum(ecpc)
            exp_norecurse = 0
            for i in xrange(1, len(ecpc)):
                print "   ", i, ecpc[i], EXPECTS[n-1]+1
                exp_norecurse += ecpc[i] * (EXPECTS[n-i]+1)
            exp_norecurse = fractions.Fraction(exp_norecurse) / (base-ecpc[0])
            exp = recursive_expected(
                    base, ecpc[0],
                    exp_norecurse)
            print "m=",base,"n=",ecpc[0],'x=',exp_norecurse,"ans=",exp
            expects.append(exp)
        EXPECTS.append(min(expects))

def split_groups(L):
    grouped = set()
    groups = []
    for i,n in enumerate(L):
        if i not in grouped:
            g = set([i])
            while n != i:
                g.add(n)
                n = L[n]
            groups.append(g)
            grouped |= g
    return groups

def group_set(L):
    groups = split_groups(L)
    group_sizes = map(len, groups)
    group_sizes.sort()
    collect_positions = count_collect_positions(L)
    assert group_sizes[:collect_positions] == [1]*collect_positions
    return tuple(group_sizes[collect_positions:])

def calc_group_exp(N):
    group_count = Counter(group_set(L) for L in
        itertools.permutations(range(N), N))
    return group_count

_FACT_CACHE=[-1]*1000
def _fact(k):
    if k < 100:
        res = _FACT_CACHE[k]
        if res >= 0:
            return res
    res = factorial(k)
    if k < 100:
        _FACT_CACHE[k] = res
    return res

def C(n, m):
    return _fact(n) / (_fact(m) * _fact(n-m))

def calc_group_c(N, groups):
    n = sum(groups)
    c = C(N, n)
    prev = 0
    count = 1
    for i in xrange(len(groups)):
        n = sum(groups[i:])
        c *= C(n, sum(groups[i+1:])) * _fact(groups[i]-1)
        if prev == groups[i]:
            count += 1
        else:
            c /= _fact(count)
            count = 1
            prev = groups[i]
    c /= _fact(count)
    return c

def group_pat_gen(N):
    groups = [()]
    start = 0
    next_ = -1
    while groups:
        g = groups.pop()
        yield g
        u = g[-1] if g else 2
        for i in xrange(u, N+1):
            ng = g + (i,)
            if sum(ng) <= N:
                groups.append(ng)


def read_problem(f):
    N = int(f.readline())
    for i in range(1, N+1):
        M = int(f.readline())
        L = [int(c)-1 for c in f.readline().split()]
        assert M == len(L)
        yield i, L

def solve(L):
    groups = split_groups(L)
    count = 0
    for g in groups:
        count += calc_expect(len(g))
    return count

def main():
    for case, problem in read_problem(fileinput.input()):
        print "Case #%d: %.6f" % (case, solve(problem))

if __name__ == '__main__':
    main()
