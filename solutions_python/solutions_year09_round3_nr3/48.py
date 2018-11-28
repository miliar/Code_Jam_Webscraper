#! /usr/bin/env python

def bestcut(cells, pending, acc=0):
    if not pending: return acc
    vals = [(p, cut(cells, p)) for p in pending]
    best = min(cl + cr for (bp, (l, (cl, cr), r)) in vals)
    return min(bestcut(l + [cl, cr] + r, pending - frozenset([bp]), acc + cl + cr)
               for (bp, (l, (cl, cr), r)) in vals if cl + cr == best)

def cut(cells, p):
    if isinstance(cells, tuple):
        cells = sum(cells, [])
    acc = 0
    i = 0
    while acc + cells[i] < p:
        acc += cells[i] + 1
        i += 1
    off = p - acc
    return cells[:i], [off - 1, cells[i] - off], cells[i + 1:]

def draw(cells, c='x'):
    if isinstance(cells, tuple):
        l, c, r = cells
        ac = [draw(l)]
        if l: ac.append(' ')
        ac.append(draw(c, 'X'))
        if r: ac.append(' ')
        ac.append(draw(r))
        return ''.join(ac)
    return ' '.join(c * n for n in cells)

if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(1, n+1):
        print 'Case #%d:' % i,
        p, q = map(int, raw_input().split())
        cells = map(int, raw_input().split())
        print bestcut([p], frozenset(cells))
