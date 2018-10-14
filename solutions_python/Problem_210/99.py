import sys
import math

f = sys.stdin

if 'DEBUG' in sys.argv:
    f = open('in.txt', 'r')

def gi():
    return int(f.readline())


def gil():
    return map(int, f.readline().strip().split())

T = 60 * 24

def fill_who(who, intv, c):
    for b, e in intv:
        for i in range(b+1, e+1):
            assert who[i] == 3
            who[i] = c

def min_swaps(a_intervs, b_intervs):
    who = [3] * (T+1) # minuty liczymy od 1
    fill_who(who, a_intervs, 0)
    fill_who(who, b_intervs, 1)

    def mkState():
        st = dict()
        st[0] = [10**9] * (T+1)
        st[1] = [10**9] * (T+1)
        return st

    st = mkState()
    tmp_st = mkState()
    st[0][0] = 0
    st[1][0] = 1

    for t in range(1, T+1):
        for w in [0, 1]:
            for k in range(T+1):
                if w == who[t]:
                    tmp_st[w][k] = 10**9
                else:
                    c1 = 10**9 if k == 0 else st[w][k-1]
                    c2 = 10**9 if t-1-(k-1) < 0 else st[1-w][t-1-(k-1)]+1
                    tmp_st[w][k] = min(c1, c2)

        st, tmp_st = tmp_st, st

    return st[0][T/2]


def read_intervs(n):
    res = []
    for _ in range(n):
        b, e = gil()
        res.append((b, e))
    return res

def solve():
    tests = gi()
    for testNr in range(1, tests + 1):
        Ai, Bi = gil()
        aint = read_intervs(Ai)
        bint = read_intervs(Bi)
        res = min(min_swaps(aint, bint), min_swaps(bint, aint))
        print "Case #%d: %d" % (testNr, res)


solve()
