# coding: utf8

def scan():
    while True:
        for w in input().split():
            yield w

words = scan()

def scans(num=-1):
    return (next(words) for i in range(num)) if num >= 0 else next(words)

def scani(num=-1):
    return (int(value) for value in scans(num)) if num >= 0 else int(scans())

def scanf(num=-1):
    return (float(value) for value in scans(num)) if num >= 0 else float(scans())

#------------------------------------------------------------------------------
for case in range(1, scani() + 1):
    res = 'YES'
    n, m = scani(2)
    s = n*m
    g = [[scani(), 100, 100, 100, 100] for i in range(s)]
    def fill(start, end, step, index):
        h = 0
        for i in range(start, end, step):
            h = max(h, g[i][0])
            g[i][index] = min(g[i][index], h)
    for i in range(0, m):
        fill(i, s, m, 1) # top to bottom
        fill(s-m+i, -1, -m, 2) # bottom to top
    for i in range(0, n):
        fill(i*m, i*m+m, 1, 3) # left to right
        fill(i*m+m-1, i*m-1, -1, 4) # right to left
    for i in range(0, s):
        if g[i][0] < min(max(g[i][1:3]), max(g[i][3:5])):
            res = 'NO'
            break
    print("Case #{0}: {1}".format(case, res))
