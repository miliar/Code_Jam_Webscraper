from sys import stdin

t = int(stdin.readline())

def check(l):
    if l.count('X') == 4 or (l.count('X') == 3 and l.count('T') == 1):
        return 1

    if l.count('O') == 4 or (l.count('O') == 3 and l.count('T') == 1):
        return 2

    if l.count('.') > 0:
        return 4
    
    return 0

for case in range(1, t+1):

    desk = []
    for i in range(4):
        desk.append(stdin.readline())

    stdin.readline()
    
    
    w = 0
    l = []
    for y in range(4):
        for x in range(4):
            l.append(desk[y][x])
        w |= check(l)
        l = []
 
    for x in range(4):
        for y in range(4):
            l.append(desk[y][x])
        w |= check(l)
        l = []

    for x in range(4):
        l.append(desk[x][x])
    w |= check(l)
    l = []

    for x in range(4):
        l.append(desk[x][3 - x])
    w |= check(l)
    l = []
    
    if w & 1:
        r = 'X won'
    elif w & 2:
        r = 'O won'
    elif w & 4:
        r = 'Game has not completed'
    else:
        r = 'Draw'


    print "Case #%d: %s" % (case, r)



