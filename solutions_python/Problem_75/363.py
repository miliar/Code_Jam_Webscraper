import itertools
from collections import defaultdict

def format_result(seq):
    return '[{}]'.format(', '.join(seq))

def parse_line(line):
    it = iter(line.split())
    cs = list(itertools.islice(it, int(next(it))))
    ds = list(itertools.islice(it, int(next(it))))
    next(it)
    return cs, ds, next(it)

def solve(combines, opposeds, seq):
    combines = build_combines(combines)
    opposeds = build_opposeds(opposeds)

    xs = ''
    for x in seq:
        c = xs[-1:] + x
        if c in combines:
            xs = xs[:-1] + combines[c]
        elif xs and x in opposeds:
            for y in opposeds[x]:
                #i = xs.rfind(y)
                #if i >= 0:
                if y in xs:
                    #xs = xs[:i]
                    xs = ''
                    break
            else:
                xs += x
        else:
            xs += x
    return xs

def build_combines(xs):
    result = {}
    for a, b, c in xs:
        result[a+b] = result[b+a] = c
    return result

def build_opposeds(xs):
    result = defaultdict(set)
    for a, b in xs:
        result[a].add(b)
        result[b].add(a)
    return result

if __name__ == '__main__':
    import sys
    for i, line in enumerate(itertools.islice(sys.stdin, 1, None), 1):
        print 'Case #{}: {}'.format(i, format_result(solve(*parse_line(line))))
