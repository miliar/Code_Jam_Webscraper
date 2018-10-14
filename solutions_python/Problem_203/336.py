#! /usr/bin/env python
cases = int(raw_input())
for case in range(0, cases):
    args = raw_input().split(' ')
    r = int(args[0])
    c = int(args[1])
    cake = []
    for i in range(0, r):
        cake.append(list(raw_input()))
    for i in range(0, r):
        b = ''
        for d in cake[i]:
            if d != '?':
                b = d
                break
        for j in range(0, c):
            if cake[i][j] == '?':
                cake[i][j] = b
            elif cake[i][j] != b:
                b = cake[i][j]
    for i in range(0, r):
        if cake[i][0] == '':
            for j in range(i+1, r):
                if cake[j][0] != '':
                    cake[i] = cake[j]
                    break
            if cake[i][0] == '':
                for j in range(i, -1, -1):
                    if cake[j][0] != '':
                        cake[i] = cake[j]
                        break

    print("Case #{}:".format(case + 1,))
    for row in cake:
        str = ""
        for i in row:
            str += i
        print str 
