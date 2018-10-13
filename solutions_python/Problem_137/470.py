#! /usr/bin/python

import sys

histPoints = []
r = 0
c = 0
m = 0

def evaluate():
    result = 0
    gameMap = [[0] * c for i in range(r)]
    #print "HIST: ", histPoints

    if r * c - m != 1:
        for coor in histPoints:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    x = coor[0] + i
                    y = coor[1] + j
                    if x < 0 or y < 0 or x >= r or y >= c:
                        continue
                    if not gameMap[x][y]:
                        gameMap[x][y] = 1
                        result += 1
        ret = r * c - result - m
    else:
        gameMap[0][0] = 1
        ret = 0
    #print "TOTAL: %d, RES: %d, Mine: %d" % (r * c, result, m)
    if ret == 0:
        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    sys.stdout.write("c")
                    continue
                if gameMap[i][j]:
                    sys.stdout.write(".")
                else:
                    sys.stdout.write("*")
            sys.stdout.write("\n")
    return ret

def trial(point):
#    print "trying", point
    histPoints.append(point)
    ret = evaluate()
    if ret == 0:
        return True
    elif ret < 0:
        histPoints.pop()
        return False

    children = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = point[0] + i
            y = point[1] + j
            if x < 0 or y < 0 or x >= r or y >= c:
                continue
            if not (x, y) in histPoints:
                children.append((x, y))
    for child in children:
        ret = trial(child)
        if ret:
            return True
    histPoints.pop()
    return False

def solve():
    if not trial((0, 0)):
        print "Impossible"

fh = open(sys.argv[1])

T = int(fh.readline())

for i in range(T):
    print "Case #%d:" % (i + 1)
    (r, c, m) = [int(token) for token in fh.readline().split()]
    histPoints = list()
    solve()

