from sys import stdin

def solve(t):
    line = stdin.readline().split(' ')
    n = int(line[0])
    v = [0, 0, 0]
    add = [0, 0, 0]
    v[0] = (int(line[1]), 'R')
    v[1] = (int(line[3]), 'Y')
    v[2] = (int(line[5]), 'B')

    add[0] = (int(line[4]), 'G')
    add[1] = (int(line[6]), 'V')
    add[2] = (int(line[2]), 'O')

    # Special cases

    for k in range (0, 3):
        zer = True
        for kk in range(0, 3):
            if kk != k:
                if v[kk][0] != 0 or add[kk][0] != 0:
                    zer = False
        if not zer:
            continue
        res = ''
        if v[k][0] == add[k][0]:
            for i in range(v[k][0]):
                res += v[k][1] + add[k][1]
        else:
            res = 'IMPOSSIBLE'
        print('Case #' + str(t + 1) + ': ' + res)
        return


    more = False
    for i in range(0, 3):
        if add[i][0] >= v[i][0] and add[i][0] > 0:
            more = True

    if more:
        print('Case #' + str(t + 1) + ': IMPOSSIBLE')
        return

    s = v.copy()
    s[0] = (s[0][0] - add[0][0], 'R', 0)
    s[1] = (s[1][0] - add[1][0], 'Y', 1)
    s[2] = (s[2][0] - add[2][0], 'B', 2)
    s.sort()

    a = s[0][0]
    b = s[1][0]
    c = s[2][0]

    # print(str(a) + ' ' + str(b) + ' ' + str(c))

    res = ''
    if a + b < c:
        res = 'IMPOSSIBLE'
    else:
        for i in range(0, c):
            if i == 0:
                for j in range(0, add[s[2][2]][0]):
                    res += s[2][1] + add[s[2][2]][1]
                res += s[2][1]
            else:
                res += s[2][1]

            if i < a:
                if i == 0:
                    for j in range(0, add[s[0][2]][0]):
                        res += s[0][1] + add[s[0][2]][1]
                    res += s[0][1]
                else:
                    res += s[0][1]
            if i >= c - b:
                if i == c - b:
                    for j in range(0, add[s[1][2]][0]):
                        res += s[1][1] + add[s[1][2]][1]
                    res += s[1][1]
                else:
                    res += s[1][1]

    print('Case #' + str(t + 1) + ': ' + res)

T = int(stdin.readline())
for t in range(0, T):
    solve(t)
