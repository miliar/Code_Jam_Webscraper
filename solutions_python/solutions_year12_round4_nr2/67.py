def solve(w, l, rs):
    rs = sorted([(r, i) for i,r in enumerate(rs)])
    flip = w < l
    if flip:
        w, l = l, w
    def pack_top():
        results = []
        x = -rs[-1][0]
        y = rs[-1][0]
        while rs:
            r = rs[-1][0]
            if x + r <= w:
                _,i=rs.pop()
                results.append((i, x+r, 0))
                x += 2*r
            else:
                break
        return y, results
    def pack_row(y, results):
        x = -rs[-1][0]
        y += rs[-1][0]
        y2 = y + rs[-1][0]
        while rs:
            r = rs[-1][0]
            if x + r <= w:
                _,i = rs.pop()
                results.append((i, x+r, y))
                x += 2*r
            else:
                break
        return y2

    y, results = pack_top()
    if rs:
        results.extend((i,x,l) for i,x,_ in pack_top()[1])
    while rs:
        y = pack_row(y, results)

    if flip:
        results = [(i,y,x) for i,x,y in results]
    return ' '.join('%d %d' % (x,y) for (i,x,y) in sorted(results))

rd = raw_input
for t in range(1, 1+int(rd())):
    _, w, l = map(int, rd().split())
    print 'Case #%d: %s' % (t, solve(w, l, map(int, rd().split())))
