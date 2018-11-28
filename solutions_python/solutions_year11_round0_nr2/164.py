import sys

tokens = sys.stdin.read().split()
tokens.reverse()

TT = int(tokens.pop())
for nt in xrange(TT):
    combines = {}
    opposed = set()

    C = int(tokens.pop())
    for _ in xrange(C):
        tok = tokens.pop()
        combines[(tok[0], tok[1])] = tok[2]
        combines[(tok[1], tok[0])] = tok[2]

    D = int(tokens.pop())
    for _ in xrange(D):
        tok = tokens.pop()
        opposed.add((tok[0], tok[1]))
        opposed.add((tok[1], tok[0]))

    _ = tokens.pop()
    el = []
    for ch in tokens.pop():
        el.append(ch)
        while len(el) >= 2 and (el[-2], el[-1]) in combines:
            ch = combines[(el[-2], el[-1])]
            el.pop()
            el.pop()
            el.append(ch)

        for i in xrange(len(el)-1):
            if (el[i], ch) in opposed:
                el = []
                break

    output = '['+', '.join(el)+']'
    print 'Case #%d: %s' % (nt+1, output)
