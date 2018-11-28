#!/home/balazs/anaconda2/bin/python

import copy
import operator

t = int(raw_input())
for i in xrange(t):
    n, r, o, y, g, b, v = map(int, raw_input().split(' '))

    colors = {'R': r, 'Y': y, 'B': b}
    colors = {k: v for k, v in colors.iteritems() if v}

    resp = []
    impossible = False
    for _ in range(n):
        _colors = copy.copy(colors)
        if resp and resp[-1] in _colors:
            del _colors[resp[-1]]
        if not _colors:
            impossible = True
            break
        resp.append(max(_colors.iteritems(), key=operator.itemgetter(1))[0])
        colors[resp[-1]] -= 1
        if colors[resp[-1]] == 0:
            del colors[resp[-1]]

    # colors = [r, y, b]
    # resp = []
    # prev = None
    # for _ in range(n):
    #     _colors = copy.copy(colors)
    #     if prev is not None:
    #         del _colors[prev]
    #     idx = _colors.index(max(_colors))
    #     colors[idx] -= 1
    #     resp.append("RYB"[idx])
    #     prev = idx

    if impossible:
        resp = "IMPOSSIBLE"
    elif resp[0] == resp[-1]:
        if len(resp) >= 3 and resp[-3] != resp[-1]:
            resp[-2], resp[-1] = resp[-1], resp[-2]
            resp = ''.join(resp)
        else:
            resp = "IMPOSSIBLE"
    else:
        resp = ''.join(resp)
    print "Case #{}: {}".format(i + 1, resp)

