import os

def rotate(n, lines):
    for i in xrange(n):
        lines[i] = lines[i].replace(".","")
        lines[i] = "." * (n - len(lines[i])) + lines[i]

    new = [[0 for col in range(n)] for row in range(n)]
    for i in xrange(n):
        for j in xrange(n):
            new[i][j] = lines[n - j - 1][i]
    return new

def checkwin(n, k, lines):
    red = False
    blue = False
    for i in xrange(n):
        for j in xrange(n):
            t = lines[i][j]
            if t <> ".":
                twin = True
                for l in xrange(k - 1):
                    if (j + l + 1 >= n):
                        twin = False
                    else:
                        if (lines[i][j + l + 1] <> t):
                            twin = False
                if not twin:
                    twin = True
                    for l in xrange(k - 1):
                        if (i + l + 1 >= n):
                            twin = False
                        else:
                            if (lines[i + l + 1][j] <> t):
                                twin = False
                if not twin:
                    twin = True
                    for l in xrange(k - 1):
                        if (i + l + 1 >= n) or (j + l + 1 >= n):
                            twin = False
                        else:
                            if (lines[i + l + 1][j + l + 1] <> t):
                                twin = False
                if not twin:
                    twin = True
                    for l in xrange(k - 1):
                        if (i + l + 1 >= n) or (j - l - 1 < 0):
                            twin = False
                        else:
                            if (lines[i + l + 1][j - l - 1] <> t):
                                twin = False
                if twin:
                    if t == "R":
                        red = True
                    else:
                        blue = True
    if red and blue:
        return "Both"
    if red:
        return "Red"
    if blue:
        return "Blue"
    return "Neither"

t = input()

for i in xrange(t):
    n, k = map(int, raw_input().split())
    print "Case #%d:" % (i+1),
    lines = []
    for j in xrange(n):
        lines.append(raw_input())
    lines = rotate(n, lines)
    print checkwin(n, k, lines)
    