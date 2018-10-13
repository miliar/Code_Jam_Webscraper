def iter_problem_set(fname):
    with open(fname, 'rb') as f:
        count = int(next(f))
        googlers = []

        for l in f:
            v = map(int, l.split(' '))
            yield (v[0], v[1], v[2], v[3:])

with open('B-large.out','w') as fout:
    for (idx, (N, S, p, googlers)) in enumerate(iter_problem_set('B-large.in')):
        case = idx + 1

        no_suprise_map = {
            0: lambda x: (x/3, x/3, x/3),
            1: lambda x: (x/3+1, x/3, x/3),
            2: lambda x: (x/3+1, x/3+1, x/3),
            }

        suprise_map = {
            0: lambda x: (x/3+1, x/3, x/3-1),
            1: lambda x: None,
            2: lambda x: (x/3+2, x/3, x/3),
            }

        for g in googlers:
            if g <= 0:
                
                continue
            no_sup = no_suprise_map[g % 3](g)
            assert(g == sum(no_sup))
            assert(max(no_sup)-min(no_sup) <= 1)
            sup = suprise_map[g % 3](g)

            if sup is not None:
                assert(g == sum(sup))
                assert(max(sup)-min(sup) == 2)

        p_no_suprise = [max(no_suprise_map[x % 3](x))-p for x in googlers if x > 0]
        p_suprise = map(lambda x: max(x) - p, filter(None, [suprise_map[x % 3](x) for x in googlers if x > 0]))

        base = sum(1 if v >= 0 else 0 for v in p_no_suprise)
        max_good_suprise = sum(1 for v in p_suprise if v is not None and v == 0)
        base += min(S, max_good_suprise)
        if p == 0:
            # Damn special case
            base += sum(1 for g in googlers if g == 0)

        fout.write('Case #%d: %d\n' % (case, base))
