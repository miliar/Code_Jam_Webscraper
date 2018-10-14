import sys

def can_cut(cut, m, Ps):
    lim = m - cut
    p = 0
    while p < len(Ps):
        if cut == 0:
            break
        n = Ps[p] / lim
        if Ps[p] % lim == 0:
            n -= 1
        if n > cut:
            return False
        p += 1
        cut -= n
    return all(P <= lim for P in Ps[p:])

def can_make_it(m, Ps):
    for cut in range(m):
        if can_cut(cut, m, Ps):
            return True
    return False

def min_minutes(Ps):
    b, e = 1, max(Ps)
    mm = e
    while b <= e:
        m = (b + e) / 2
        if can_make_it(m, Ps):
            mm = min(mm, m)
            e = m - 1
        else:
            b = m + 1
    return mm

if __name__ == '__main__':
    T = input()
    for t in range(T):
        dummy = input()
        Ps = map(int, sys.stdin.readline().split())
        print 'Case #{0}: {1}'.format(t+1, min_minutes(Ps))
