import sys

def check(m):
    may_draw = False
    for i in range(4):
        x = 0
        o = 0
        for j in range(4):
            if m[i][j] == 'X':
                x += 1
            elif m[i][j] == 'O':
                o += 1
            elif m[i][j] == 'T':
                x += 1
                o += 1
            else:
                may_draw = True
        if x == 4:
            return 1
        elif o == 4:
            return -1
    for j in range(4):
        x = 0
        o = 0
        for i in range(4):
            if m[i][j] == 'X':
                x += 1
            elif m[i][j] == 'O':
                o += 1
            elif m[i][j] == 'T':
                x += 1
                o += 1
            else:
                may_draw = True
        if x == 4:
            return 1
        elif o == 4:
            return -1
    x = 0
    o = 0
    for i in range(4):
        if m[i][i] == 'X':
            x += 1
        elif m[i][i] == 'O':
            o += 1
        elif m[i][i] == 'T':
            x += 1
            o += 1
    if x == 4:
        return 1
    elif o == 4:
        return -1
    x = 0
    o = 0
    for i in range(4):
        if m[i][3 - i] == 'X':
            x += 1
        elif m[i][3 - i] == 'O':
            o += 1
        elif m[i][3 - i] == 'T':
            x += 1
            o += 1
    if x == 4:
        return 1
    elif o == 4:
        return -1
    if may_draw:
        return -2
    else:
        return 0

def main():
    n = int(sys.stdin.readline())
    for k in range(n):
        m = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(4):
            line = sys.stdin.readline()
            for j in range(4):
                m[i][j] = line[j]
        result = check(m)
        if result == 1:
            print 'Case #{}: X won'.format(k + 1)
        elif result == 0:
            print 'Case #{}: Draw'.format(k + 1)
        elif result == -1:
            print 'Case #{}: O won'.format(k + 1)
        else:
            print 'Case #{}: Game has not completed'.format(k + 1)
        line = sys.stdin.readline()

main()