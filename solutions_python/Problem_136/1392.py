inp = open('b-in', 'r')
out = open('b-out', 'w')

cases = int(inp.next())
for case in xrange(cases):
    c, f, x = map(float, inp.next().strip().split())
    rate = 2
    best = x / rate
    at = c / rate
    while at < best:
        # print 'at: {}'.format(at)
        rate += f
        cost = x / rate
        # print 'cost: {}'.format(cost)
        best = min(best, at + cost)
        # print 'best: {}'.format(best)
        at += c / rate
    out.write('Case #{}: {:.7f}\n'.format(case + 1, best))
