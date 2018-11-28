n = int(input())
for t in range(n):
    X = 0
    O = 0
    DOT = 0
    Q = ''
    W = ''
    a = []
    for i in range(4):
        a.append(input())
    input()
    b = []
    for i in range(4):
        s = ''
        for j in range(4):
            s += a[j][i]
        b.append(s)
    for i in range(4):
        if a[i].count('X') + a[i].count('T') == 4:
            X = 1
        if a[i].count('O') + a[i].count('T') == 4:
            O = 1
        if b[i].count('X') + b[i].count('T') == 4:
            X = 1
        if b[i].count('O') + b[i].count('T') == 4:
            O = 1
        if a[i].count('.') > 0 or b[i].count('.') > 0:
            DOT = 1
        Q += a[i][i]
        W += a[i][3 - i]
    if Q.count('X') + Q.count('T') == 4:
        X = 1
    if Q.count('O') + Q.count('T') == 4:
        O = 1
    if W.count('X') + W.count('T') == 4:
        X = 1
    if W.count('O') + W.count('T') == 4:
        O = 1
    print('Case #$: '.replace('$', str(t + 1)), end = '')
    if X == 1:
        print('X won')
    if O == 1:
        print('O won')
    if X == 0 and O == 0 and DOT == 0:
        print('Draw')
    if X == 0 and O == 0 and DOT > 0:
        print('Game has not completed')
