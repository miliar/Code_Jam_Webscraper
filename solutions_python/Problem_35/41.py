import itertools
def f(i, o, y, x, h, w, v):
    _min = min(i[y + dy][x + dx] for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)] if 0 <= y + dy < h and 0 <= x + dx < w)
    for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        _y, _x = y + dy, x + dx
        if 0 <= _y < h and 0 <= _x < w and i[_y][_x] < i[y][x] and i[_y][_x] == _min:
            if o[_y][_x] >= 0 and o[_y][_x] != v:
                _n = o[_y][_x]
                for __y, __x in itertools.product(xrange(h), xrange(w)):
                    if o[__y][__x] == _n:
                        o[__y][__x] = v
            o[_y][_x] = v
            f(i, o, _y, _x, h, w, v)
            return

t = int(raw_input())
for x in xrange(1, t + 1):
    h, w = map(int, raw_input().split())
    i = list(map(int, raw_input().split()) for x in xrange(h))
    o = list(list(-1 for x in xrange(w)) for x in xrange(h))
    if h == 1 and w == 1:
        print 'Case #%d:' % x
        print 'a'
        continue
    for _y, _x in itertools.product(xrange(h), xrange(w)):
        if o[_y][_x] == -1:
            v = _y * w + _x
            o[_y][_x] = v
            f(i, o, _y, _x, h, w, v)
    letters = iter('abcdefghijklmnopqrstuvwxyz')
    for _y, _x in itertools.product(xrange(h), xrange(w)):
        if type(o[_y][_x]) is int:
            letter = letters.next()
            _n = o[_y][_x]
            for __y, __x in itertools.product(xrange(h), xrange(w)):
                if o[__y][__x] == _n:
                    o[__y][__x] = letter
    print 'Case #%d:' % x
    for y in o:
        print ' '.join(x for x in y)
