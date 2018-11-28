import sys

def run(): # {{{
    inp=sys.argv[1]
    outp="%s.out" % inp.split(".")[0]

    with open(inp, 'r') as _file, open(outp, 'w') as out:
        _cases = int(_file.readline())
        for _case in range(_cases):
            print("Solving case %s" % (_case+1))
            ns, vs, xs = tuple([x for x in _file.readline().split(" ")])
            n, v, x = int(ns), float(vs), float(xs)
            sources = []
            for i in range(n):
                sources.append(tuple([float(x) for x in _file.readline().split(" ")]))
            out.write("Case #%s: %s\n" % (_case+1, _format(solve_large(n, v, x, sources))))
# }}}

def _format(result):
    return result

IMPOSSIBLE = "IMPOSSIBLE"

def solve(n, v, x, sources):
    if n>3: return IMPOSSIBLE  #TODO large input
    if n == 1:
        if x == sources[0][1]: return v/sources[0][0]
        else: return IMPOSSIBLE

    r1, c1 = sources[0]
    r2, c2 = sources[1]
    dc1, dc2 = c1 - x, c2 - x
    if dc1 > 0 and dc2 > 0: return IMPOSSIBLE
    if dc1 < 0 and dc2 < 0: return IMPOSSIBLE

    if dc1 > dc2:
        posr, posc = (r1, dc1)
        negr, negc = (r2, dc2)
    else:
        posr, posc = (r2, dc2)
        negr, negc = (r1, dc1)
    if posr*posc + negr*negc == 0:
        return v / (negr + posr)
    if posr*posc + negr*negc > 0:
        return v * posc / (negr*(posc-negc))
    else:
        return v * negc / (posr*(negc-posc))

def solve_large(n, v, x, sources):
    res_rate = 0
    colder = []
    hotter = []
    for r, c in sources:
        if c == x: res_rate += r
        if c < x: colder.append((x-c, r))
        if c > x: hotter.append((c-x, r))
    colder = sorted(colder)
    hotter = sorted(hotter)
    print(colder, hotter)

    while True:
        if not colder or not hotter:
            if res_rate == 0: return IMPOSSIBLE
            return v/res_rate
        ct, cr = colder.pop(0)
        ht, hr = hotter.pop(0)

        if ct*cr == ht*hr:
            res_rate += cr+hr
        elif ct*cr < ht*hr:
            _hr = cr * ct / ht
            res_rate += cr + _hr
            hotter.insert(0, (ht, hr-_hr))
        else:
            _cr = hr * ht / ct
            res_rate += _cr + hr
            colder.insert(0, (ct, cr-_cr))

run()
