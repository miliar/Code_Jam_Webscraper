import sys

def f(field):
    if any('.' not in f for f in field):
        return True
    for i in range(0, 4):
        if all(f[i] is not '.' for f in field):
            return True
    if all(field[i][3-i] is not '.' for i in range(0, 4)):
        return True
    if all(field[i][i] is not '.' for i in range(0, 4)):
        return True
    return False

n = int(raw_input())
for test in range(1, n + 1):
    field = [raw_input().strip() for i in range(0, 4)]
    raw_input()
    free = any('.' in f for f in field)
    X = f([x.replace('T', 'X').replace('O', '.') for x in field])
    O = f([x.replace('T', 'O').replace('X', '.') for x in field])
    print "Case #%d: " % test,
    if X:
        print "X won"
    elif O:
        print "O won"
    elif free:
        print "Game has not completed"
    else:
        print "Draw"



