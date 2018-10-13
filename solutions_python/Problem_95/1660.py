
from string import ascii_lowercase

code = "A-small-attempt0"

infile = code + ".in"
outfile = code + ".out"

d = {
    'a zoo': 'y qee',
    'our language is impossible to understand': 'ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'there are twenty six factorial possibilities': 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'so it is okay if you want to just give up': 'de kr kd eoya kw aej tysr re ujdr lkgc jv',
}

def gen(d):
    t = {}
    for a, b in d.iteritems():
        for ca, cb in zip(a, b):
            if ca == ' ': continue
            assert cb not in t or t[cb] == ca
            t[cb] = ca
    return t

def odd(s):
    return [c for c in ascii_lowercase if c not in s][0]

g = gen(d)
g[odd(g)] = odd(g.values())

def solve(line):
    return ''.join(g[c] if c != ' ' else ' ' for c in line)

lines = [s.strip() for s in open(infile)]
c = int(lines[0])
f = open(outfile, "w")
for i in range(1, c+1):
    r = solve(lines[i])
    print >> f, "Case #%d:" % i, r
f.close()
