f = open('first.txt')
datas = f.read().split('\n')
f.close()

nb = int(datas[0])


def result(x):
    game = datas[x:x+4]
    complete = True

    diag = [[game[0][0], game[1][1], game[2][2], game[3][3]], [game[0][3], game[1][2], game[2][1], game[3][0]]]

    for line in game:
        winX = True
        winO = True
        for c in line:
            if c == '.':
                winX = False
                complete = False
                winO = False
            elif c == 'X':
                winO = False
            elif c == 'O':
                winX = False
        if winX:
            return 0
        if winO:
            return 1

    for i in range(4):
        winX = True
        winO = True
        for j in range(4):
            c = game[j][i]
            if c == '.':
                winX = False
                complete = False
                winO = False
            elif c == 'X':
                winO = False
            elif c == 'O':
                winX = False
        if winX:
            return 0
        if winO:
            return 1
        
    for line in diag:
        winX = True
        winO = True
        for c in line:
            if c == '.':
                winX = False
                complete = False
                winO = False
            elif c == 'X':
                winO = False
            elif c == 'O':
                winX = False
        if winX:
            return 0
        if winO:
            return 1

    if complete:
        return 3
    return 2

final = ''
x = 1
for k in range(nb):
    res = result(x)
    if res == 0:
        final += 'Case #'+str(k+1)+': X won'
    if res == 1:
        final += 'Case #'+str(k+1)+': O won'
    if res == 2:
        final += 'Case #'+str(k+1)+': Game has not completed'
    if res == 3:
        final += 'Case #'+str(k+1)+': Draw'
    final += '\n'
    x += 5

f = open('firstr.txt', 'w')
f.write(final)
f.close()
