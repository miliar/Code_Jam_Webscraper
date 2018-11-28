#!/usr/bin/python
debug = 0
input = open("a.in").readlines()

for j in range(1, len(input)):
    line = input[j]
    (n, A, B, C, D, X, Y, M) = [int(x) for x in line.split()]
    mods = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    ans = 0
    for i in range(0, n):
        mods[X % 3][Y % 3] += 1
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        if debug: print X, Y
    #print mods
    for casex in mods:
        for casey in casex:
            case = casey * (casey - 1) * (casey - 2) / 6
            if debug and case: print "1)", casex, casey, case
            ans += case
    casex = [0, 1, 2]
    for casey in [[0, 0, 0], [1, 1, 1], [2, 2, 2]]:
        case = mods[casex[0]][casey[0]] * mods[casex[1]][casey[1]] * mods[casex[2]][casey[2]]
        if debug and case: print "2)", casex, casey, case
        ans += case
    casey = [0, 1, 2]
    for casex in [[0, 0, 0], [1, 1, 1], [2, 2, 2]]:
        case = mods[casex[0]][casey[0]] * mods[casex[1]][casey[1]] * mods[casex[2]][casey[2]]
        if debug and case: print "2)", casex, casey, case
        ans += case
    casex = [0, 1, 2]
    for casey in [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]:
        case = mods[casex[0]][casey[0]] * mods[casex[1]][casey[1]] * mods[casex[2]][casey[2]]
        if debug and case: print "3)", casex, casey, case
        ans += case
    print "Case #" + str(j) + ":", ans
