L, D, N = [int(e) for e in raw_input().split()]
words = []

for i in xrange(D):
    words.append(raw_input())

def parse(patt):
    ret = []
    ingroup = False
    group = []
    for c in patt:
        if c == '(':
            ingroup = True
        elif c == ')':
            ingroup = False
            ret.append(group)
            group = []
        elif ingroup:
            group.append(c)
        else:
            ret.append([c])
    return ret

def cut(i, tok, dic):
    return [w for w in dic if w[i] in tok]

for i in xrange(N):
    patt = raw_input()
    parsed = parse(patt)
    subdict = words[:]
    for (j, tok) in enumerate(parsed):
        subdict = cut(j, tok, subdict)
    print 'Case #%d: %d' % (i + 1, len(subdict))
