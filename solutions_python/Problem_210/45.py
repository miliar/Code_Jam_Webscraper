def solve(ac, aj):
    prev = None
    prevt = 0
    l = [(i, j, True) for i, j in ac]+[(i, j, False) for i, j in aj]
    l.sort()
    sp = []
    for i, j, w in l:
        sp.append((i - prevt, prev, not w))
        prevt = j
        prev = not w
    t, p, n = sp[0]
    t -= prevt - 1440
    p = prev
    sp[0] = (t, p, n)
    sp.sort()
    sp.reverse()
    c_j = 0
    for i, j, w in l:
        if w: c_j += i - j
        else: c_j += j - i
    exch = 0
    for t, p, n in sp:
        if p == n:
            if p: c_j += t
            else: c_j -= t
        else: exch += 1
    if c_j == 0:
        return exch
    elif c_j > 0:
        for t, p, n in sp:
            if p != n:
                c_j -= t
        if c_j <= 0: return exch
        for t, p, n in sp:
            if p and n:
                exch += 2
                c_j -= 2 * t
                if c_j <= 0: return exch
    else:
        for t, p, n in sp:
            if p != n:
                c_j += t
        if c_j >= 0: return exch
        for t, p, n in sp:
            if not p and not n:
                exch += 2
                c_j += 2 * t
                if c_j >= 0: return exch
    assert False

for i in range(1, int(input())+1):
    print("Case #", i, ": ", solve(*tuple([tuple(map(int, input().split())) for i in range(k)] for k in map(int, input().split()))), sep='')

