from collections import defaultdict


def solve(m):
    d = defaultdict(lambda: [])
    for i, r in enumerate(m):
        for j, c in enumerate(r):
            if c != '?':
                d[c] += [(i, j)]
    bs = {}
    for k, v in d.items():
        if len(v) > 1:
            xs = [x[0] for x in v]
            ys = [x[1] for x in v]
            xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
            for x in range(xmin, xmax + 1):
                for y in range(ymin, ymax + 1):
                    m[x][y] = k
            bs[k] = (xmin, ymin, xmax, ymax)
        else:
            bs[k] = (v[0][0], v[0][1], v[0][0], v[0][1])

    for k, (xmin, ymin, xmax, ymax) in bs.items():
        for x in range(xmin - 1, -1, -1):
            if all([m[x][y] == '?' for y in range(ymin, ymax + 1)]):
                for y in range(ymin, ymax + 1):
                    m[x][y] = k
                xmin -= 1
            else:
                break
        for x in range(xmax + 1, len(m), 1):
            if all([m[x][y] == '?' for y in range(ymin, ymax + 1)]):
                for y in range(ymin, ymax + 1):
                    m[x][y] = k
                xmax += 1
            else:
                break
        for y in range(ymin - 1, -1, -1):
            if all([m[x][y] == '?' for x in range(xmin, xmax + 1)]):
                for x in range(xmin, xmax + 1):
                    m[x][y] = k
                ymin -= 1
            else:
                break
        for y in range(ymax + 1, len(m[0]), 1):
            if all([m[x][y] == '?' for x in range(xmin, xmax + 1)]):
                for x in range(xmin, xmax + 1):
                    m[x][y] = k
                ymax += 1
            else:
                break

    return m


t = int(input())

for case in range(1, t + 1):
    r, c = map(int, input().split())
    m = [list(input()) for _ in range(r)]
    m = solve(m)
    print('Case #{}:'.format(case))
    print('\n'.join([''.join(row) for row in m]))
