from solver import solver


def small(es, ds, uv):
    assert len(uv) == 1
    u, v = uv[0]
    assert u == 1
    assert v == len(es)
    ds = [l[i+1] for i, l in enumerate(ds[:-1])]
    ce, cs = es[0]
    es = es[1:]
    return min(rec(ce, cs, es, ds))


def rec(ce, cs, es, ds, t=0, step=0, cache=None):
    if cache is None:
        cache = {}
    for i, ((e, s), d) in enumerate(zip(es, ds)):
        ce -= d
        t += d / cs
        step += 1
        if ce < 0:
            return
        if step in cache:
            tref, ceref, csref = cache[step]
            if t >= tref and ce <= ceref and cs <= csref:
                return
            cache[step] = max(t, tref), min(ce, ceref), min(cs, csref)
        else:
            cache[step] = t, ce, cs
        if e > ce or s > cs:
            yield from rec(e, s, es[i+1:], ds[i+1:], t, step, cache)
    yield t


@solver(lines_per_case="2 * int(args[0]) + int(args[1])")
def pony(lines):
    n, q = map(int, lines[0].split())
    lines = lines[1:]
    es = [tuple(map(int, line.split())) for line in lines[:n]]
    lines = lines[n:]
    ds = [tuple(map(int, line.split())) for line in lines[:n]]
    lines = lines[n:]
    uv = [tuple(map(int, line.split())) for line in lines[:q]]
    assert len(uv) == q
    return small(es, ds, uv)

if __name__ == "__main__":
    pony.from_cli()
