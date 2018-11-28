import sys

def count_recyled(from_, to):
    in_range = lambda x: x <= to and from_ <= x
    c = 0
    used = set()
    for n in xrange(from_, to+1):
        nstr = str(n)
        for p in xrange(1, len(nstr)):
            m = nstr[-p:] + nstr[:-p]
            if m.startswith('0'):
                continue
            if n >= int(m):
                continue
            if in_range(int(m)) and (n,m) not in used:
                c += 1
                used.add((n, m))

    return c

def get_borders(line):
    a, b = line.split()
    return int(a), int(b)

with open(sys.argv[1]) as fp:
    data = fp.read()
    lines = data.splitlines()[1:]
    for line_number, line in enumerate(lines):
        print('Case #%s: %s' % (line_number+1, count_recyled(*get_borders(line))))
