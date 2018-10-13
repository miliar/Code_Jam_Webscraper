import argparse, math

ap = argparse.ArgumentParser()
ap.add_argument('input', type=argparse.FileType('r'))
args = ap.parse_args()
toks = args.input.read().split()
toks.reverse()

T = int(toks.pop())
for t in xrange(T):
    R = int(toks.pop())
    C = int(toks.pop())

    map = [list(toks.pop()) for i in xrange(R)]

    def get(x, y):
        return map[y][x]

    turrets = []
    needs = {}
    for y in xrange(R):
        row = map[y]
        for x in xrange(C):
            if row[x] in '|-':
                turrets.append((x, y))
            elif row[x] == '.':
                needs[(x, y)] = set()

    def trace(x, y, dx, dy):
        reqs = set()

        while True:
            x += dx
            y += dy

            if x >= C or y >= R or x < 0 or y < 0:
                return reqs

            ch = get(x, y)
            if ch in '-|':
                return None
            if ch == '#':
                return reqs

            if ch == '/':
                dx, dy = -dy, -dx
            elif ch == '\\':
                dx, dy = dy, dx
            elif ch == '.':
                reqs.add((x, y))

    res = {}
    choose = []
    impos = False
    for i, (x, y) in enumerate(turrets):
        r1 = trace(x, y, 1, 0)
        r2 = trace(x, y, -1, 0)
        r3 = trace(x, y, 0, 1)
        r4 = trace(x, y, 0, -1)

        horiz = r1 is not None and r2 is not None
        vert = r3 is not None and r4 is not None

        if not horiz and not vert:
            impos = True
            break

        if not horiz:
            res[i] = '|'
        elif not vert:
            res[i] = '-'
        else:
            choose.append(i)

        if horiz:
            for xx, yy in r1:
                needs[xx, yy].add((i, '-'))
            for xx, yy in r2:
                needs[xx, yy].add((i, '-'))

        if vert:
            for xx, yy in r3:
                needs[xx, yy].add((i, '|'))
            for xx, yy in r4:
                needs[xx, yy].add((i, '|'))

    if impos:
        print 'Case #{}: IMPOSSIBLE'.format(t + 1)
        continue

    def satis_one(x, y):
        return any(res.get(i, dir) == dir for i, dir in needs[x, y])

    def satis_all():
        return all(satis_one(x, y) for x, y in needs.iterkeys())

    def go():
        if not choose:
            return satis_all()

        i = choose.pop()
        res[i] = '-'
        if satis_all() and go():
            return True
        res[i] = '|'
        return satis_all() and go()

    if not go():
        print 'Case #{}: IMPOSSIBLE'.format(t + 1)
        continue

    for i, dir in res.iteritems():
        x, y = turrets[i]
        map[y][x] = dir

    print 'Case #{}: POSSIBLE'.format(t + 1)
    for row in map:
        print ''.join(row)
