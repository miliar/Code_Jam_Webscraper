#!/usr/bin/env python
# Python 2.6.6

t = int(raw_input())

for tc in xrange(1, t+1):
    r, c = map(int, raw_input().split())
    case = []
    for i in xrange(r):
        case.append(list(raw_input()))
    impossible = False
    for i in xrange(r):
        for j in xrange(c):
            if case[i][j] == '#':
                if (i == r-1) or (j == c-1):
                    impossible = True
                    break
                elif (case[i+1][j] == '#') and (case[i][j+1] == '#') and (case[i+1][j+1] == '#'):
                    case[i][j] = '/'
                    case[i+1][j] = '\\'
                    case[i][j+1] = '\\'
                    case[i+1][j+1] = '/'
                else:
                    impossible = True
                    break
        if impossible:
            break
    print("Case #%d:" % tc)
    if impossible:
        print("Impossible")
    else:
        for i in xrange(r):
            print("".join(case[i]))
