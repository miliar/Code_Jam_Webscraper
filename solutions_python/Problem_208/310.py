from itertools import accumulate

rd = input

def ints():
    return list(map(int, rd().split()))

def solve(ess, ds):
    D = sum(ds)
    ds = [0]+list(accumulate(ds))
    rs = {}
    def _solve(k):
        if k in rs:
            pass
        elif k == 0:
            rs[k] = 0
        else:
            r = min((_solve(j) + (ds[k] - ds[j])/ess[j][1])
                    for j in range(k)
                    if ess[j][0] >= (ds[k]-ds[j]))
            rs[k] = r
        return rs[k]
              
    return _solve(len(ds)-1)

for t in range(int(rd())):
    n, q = ints()
    assert q == 1
    ess = [ints() for _ in range(n)]
    ds = [ints() for _ in range(n)]
    u, v = ints()
    assert u == 1 and v == n
    print('Case #{}: {}'.format(
        t+1,
        solve(ess, [ds[i][i+1] for i in range(n-1)])))
