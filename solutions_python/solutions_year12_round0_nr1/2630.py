prob = 'A-test'
prob = 'A-small-attempt0'

f = open('%s.in' % prob, 'r')
text = f.read()
f.close()

w = open('%s.out' % prob, 'w')

lines = text.split('\n')
N = int(lines[0])

G = list('ynficwl kuomxsev pdrjgtha ')
E = list('abcdefghijklmnopqrstuvwxyz')

for i in range(1,N+1):
    g = lines[i].strip().lower()
    if not g:
        continue
    g = list(g)
    e = list(g)

    for ii in range(0,len(g)):
        if not g[ii].strip():
            continue
        if g[ii] in G:
            e[ii] = E[G.index(g[ii])]
        else:
            blank = G.index(' ')
            if blank != -1:
                G[blank] = g[ii]
                e[ii] = E[blank]

    o = 'Case #%s: %s' % (i, ''.join(e))
    print o
    w.write('%s\n' % o)
    w.flush()

w.close()