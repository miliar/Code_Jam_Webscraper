from collections import Counter
T = int(input())

for i in range(T):
    res = list()
    a = [[str(x) for x in input()], [str(x) for x in input()], [str(x) for x in input()], [str(x) for x in input()]]
    #print(a)
    if i < T - 1:
        blank = input()

    line1 = Counter(a[0])
    line2 = Counter(a[1])
    line3 = Counter(a[2])
    line4 = Counter(a[3])

    c1 = Counter([a[0][0], a[1][0], a[2][0], a[3][0]])
    c2 = Counter([a[0][1], a[1][1], a[2][1], a[3][1]])
    c3 = Counter([a[0][2], a[1][2], a[2][2], a[3][2]])
    c4 = Counter([a[0][3], a[1][3], a[2][3], a[3][3]])

    d1 = Counter([a[0][0], a[1][1], a[2][2], a[3][3]])
    d2 = Counter([a[0][3], a[1][2], a[2][1], a[3][0]])

    #Line 1
    if line1['X'] >=3 and line1['T'] >= 1:
        res.append('X won')
    elif line1['X'] == 4:
        res.append('X won')

    if line1['O'] >=3 and line1['T'] >= 1:
        res.append('O won')
    elif line1['O'] == 4:
        res.append('O won')

    #line2
    if line2['X'] >=3 and line2['T'] >= 1:
        res.append('X won')
    elif line2['X'] == 4:
        res.append('X won')

    if line2['O'] >=3 and line2['T'] >= 1:
        res.append('O won')
    elif line2['O'] == 4:
        res.append('O won')

    #line3
    if line3['X'] >=3 and line3['T'] >= 1:
        res.append('X won')
    elif line3['X'] == 4:
        res.append('X won')

    if line3['O'] >=3 and line3['T'] >= 1:
        res.append('O won')
    elif line3['O'] == 4:
        res.append('O won')

    #line3
    if line4['X'] >=3 and line4['T'] >= 1:
        res.append('X won')
    elif line4['X'] == 4:
        res.append('X won')

    if line4['O'] >=3 and line4['T'] >= 1:
        res.append('O won')
    elif line4['O'] == 4:
        res.append('O won')


    #collones
    #colone 1
    if c1['X'] >=3 and c1['T'] >= 1:
        res.append('X won')
    elif c1['X'] == 4:
        res.append('X won')

    if c1['O'] >=3 and c1['T'] >= 1:
        res.append('O won')
    elif c1['O'] == 4:
        res.append('O won')

    #colone 2
    if c2['X'] >=3 and c2['T'] >= 1:
        res.append('X won')
    elif c2['X'] == 4:
        res.append('X won')

    if c2['O'] >=3 and c2['T'] >= 1:
        res.append('O won')
    elif c2['O'] == 4:
        res.append('O won')

    #colone 3
    if c3['X'] >=3 and c3['T'] >= 1:
        res.append('X won')
    elif c3['X'] == 4:
        res.append('X won')

    if c3['O'] >=3 and c3['T'] >= 1:
        res.append('O won')
    elif c3['O'] == 4:
        res.append('O won')

    #colone 3
    if c4['X'] >=3 and c4['T'] >= 1:
        res.append('X won')
    elif line4['X'] == 4:
        res.append('X won')

    if c4['O'] >=3 and c4['T'] >= 1:
        res.append('O won')
    elif c4['O'] == 4:
        res.append('O won')

    #diagonales
    #diagonale1
    if d1['X'] >=3 and d1['T'] >= 1:
        res.append('X won')
    elif d1['X'] == 4:
        res.append('X won')

    if d1['O'] >=3 and d1['T'] >= 1:
        res.append('O won')
    elif d1['O'] == 4:
        res.append('O won')

    #d2
    if d2['X'] >=3 and d2['T'] >= 1:
        res.append('X won')
    elif d2['X'] == 4:
        res.append('X won')

    if d2['O'] >=3 and d2['T'] >= 1:
        res.append('O won')
    elif d2['O'] == 4:
        res.append('O won')

    if not res:
        if (line1['.'] or line2['.'] or line3['.'] or line4['.']) >= 1:
            print('Case #' + str(i+1) + ': Game has not completed')
        else:
            print('Case #' + str(i+1) + ': Draw')
    else:
        print('Case #' + str(i+1) + ': ' + res[0])