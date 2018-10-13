import sys


def xy_to_diag(x, y):
    return x+y, x-y


def diag_to_xy(d1, d2):
    return int((d1+d2)/2), int((d1-d2)/2)


def fb_trav(it):
    for i in range(int((len(it)+1)/2)):
        yield it[i]
        yield it[len(it)-1-i]


def diags(d1, n):
    for x in range(1, n+1):
        y = d1 - x
        if 1 <= x <= n and 1 <= y <= n:
            yield x - y


def get_pos(n, pos):
    d1s = [x + y for x, y in pos]
    d2s = [x - y for x, y in pos]

    for d1 in range(2, 2*n+1):
        if d1 in d1s:
            continue
        for d2 in fb_trav(list(diags(d1, n))):
            if d2 not in d2s:
                yield diag_to_xy(d1, d2)
                d2s += [d2]
                break


def get_xos(n, xos):
    xs, ys = set(), set()
    for i in range(1, n+1):
        xs.add(i)
        ys.add(i)
    for x, y in xos:
        xs.remove(x)
        ys.remove(y)
    return zip(list(xs), list(ys))


def lens(*args):
    return sum([len(x) for x in args])


def solve(n, xos, pos):
    new_xos = list(get_xos(n, xos))
    new_pos = list(get_pos(n, pos))

    points = lens(xos, pos, new_pos, new_xos)

    new_oos = []
    for xo in list(new_xos):
        if xo in pos + new_pos:
            new_oos += [xo]
            new_xos.remove(xo)
        if xo in new_pos:
            new_pos.remove(xo)

    for po in list(new_pos):
        if po in xos:
            new_oos += [po]
            new_pos.remove(po)

    print('{} {}'.format(points,
                         lens(new_pos, new_xos, new_oos)))

    for x, y in new_pos:
        print('+ {} {}'.format(x, y))
    for x, y in new_xos:
        print('x {} {}'.format(x, y))
    for x, y in new_oos:
        print('o {} {}'.format(x, y))

file_name = sys.argv[1]
with open(file_name) as file:
    T = int(file.readline())
    for i in range(T):
        N, M = file.readline().split(' ')
        N, M = int(N), int(M)
        xos, pos = [], []
        for j in range(M):
            c, x, y = file.readline().split(' ')
            x, y = int(x), int(y)
            if c != '+':
                xos += [(x, y)]
            if c != 'x':
                pos += [(x, y)]
        print('Case #{}: '.format(i+1), end='')
        solve(N, xos, pos)
