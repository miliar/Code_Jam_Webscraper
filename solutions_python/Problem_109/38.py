#!/usr/bin/python

import sys

def solve(N, W, L, students):
    corners = set([(0, 0)])
    locs = {}
    ordered_students = list(enumerate(students))
    ordered_students.sort(key=lambda a: -a[1])

    for j, r in ordered_students:
        for x, y in corners:
            px = x
            py = y
            newx = x + r
            if x > 0:
                px += r
                newx += r
            newy = y + r
            if y > 0:
                py += r
                newy += r
            if px > W:
                continue
            if py > L:
                continue

            good = True
            for i, (lx, ly) in locs.items():
                if (lx - px) ** 2 + (ly - py) ** 2 < (r + students[i]) ** 2:
                    good = False
                    break
            if not good:
                continue

            locs[j] = (px, py)
            corners.remove((x, y))
            corners.add((newx, y))
            corners.add((x, newy))
            break
        else:
            print W, L
            print r, students
            print corners
            print locs
            sys.stderr.write('error\n')
            sys.exit(1)

    return ' '.join('%s %s' % l for l in (locs[k] for k in range(N)))

T = int(raw_input())
for i in range(T):
    N, W, L = map(int, raw_input().split())
    print "Case #%i: %s" % (i+1, solve(N, W, L, map(int, raw_input().split())))
    sys.stdout.flush()
