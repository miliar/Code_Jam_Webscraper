
import sys
from collections import deque

def fmtit(x):
    return ('%f' % x).rstrip('0').rstrip('.')

casenum = 1
def doit():
    global lines
    global casenum

    N, W, L = map(int, lines.popleft().split(" "))
    shapes = map(lambda x: {'r' : int(x)}, lines.popleft().split(" "))

    for i in range(len(shapes)):
        shapes[i]['i'] = i

    shapes.sort(reverse=True, key=lambda x: x['r']);

    shapes[0].update({
        'x' : 0,
        'y' : 0
    })

    x = 0
    y = 0

    rowstart = 0
    fail = False

    for i in range(1, len(shapes)):
        prev = shapes[i-1]
        cur = shapes[i]

        x += prev['r'] + cur['r'] 

        if x > W:
            x = 0
            y += shapes[rowstart]['r'] + cur['r']
            rowstart = i

            if y > L:
                fail = True
                break

        shapes[i].update({
            'x' : x,
            'y' : y
        })

    # print W, L, shapes

    # Try opposite direction traversal
    if fail:
        x = 0
        y = 0

        colstart = 0

        fail = False
        for i in range(1, len(shapes)):
            prev = shapes[i-1]
            cur = shapes[i]

            y += prev['r'] + cur['r']

            if y > L:
                y = 0
                x += shapes[colstart]['r'] + cur['r']
                colstart = i

                if y > L:
                    fail = True
                    break

            shapes[i].update({
                'x' : x,
                'y' : y
            })

    if fail:
        print "FAIL: case %d" % casenum
        sys.exit(0)

    output = [{}] * N

    for shape in shapes:
        output[shape['i']] = shape

    print 'Case #%d:' % (casenum),
    print ' '.join(["%s %s" % (fmtit(a['x']), fmtit(a['y'])) for a in output])
    casenum += 1

lines = deque([x.strip() for x in sys.stdin.readlines()])
ZZZ = int(lines.popleft())
for case in range(ZZZ):
    doit()
