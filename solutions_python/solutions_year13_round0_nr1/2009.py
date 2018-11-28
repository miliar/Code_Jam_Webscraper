import math
cases = int(input())

index = 0
l = [['.', '.', '.', '.',], ['.', '.', '.', '.',], ['.', '.', '.', '.',], ['.', '.', '.', '.',]]

def can_win(lx):
    if '.' in lx:
        return False
    if 'O' in lx and 'X' in lx:
        return False
    return True

while index < cases:
    result = ''
    may_draw = True
    for i in range(4):
        s = raw_input()
        for j in range(4):
            if s[j] == '.':
                may_draw = False
            l[i][j] = s[j]
    s = raw_input()

    if can_win([l[0][0], l[1][1], l[2][2], l[3][3]]):
        c = l[0][0]
        if c == 'T':
            c = l[1][1]
        result = "Case #%d: %s won" % (index+1, c)
    elif can_win([l[0][3], l[1][2], l[2][1], l[3][0]]):
        c = l[0][3]
        if c == 'T':
            c = l[1][2]
        result = "Case #%d: %s won" % (index+1, c)

    if result:
        print result
        index += 1
        continue

    for i in range(4):
        if can_win([l[i][0], l[i][1], l[i][2], l[i][3]]):
            c = l[i][0]
            if c == 'T':
                c = l[i][1]
            result = "Case #%d: %s won" % (index+1, c)
            break

        if can_win([l[0][i], l[1][i], l[2][i], l[3][i]]):
            c = l[0][i]
            if c == 'T':
                c = l[1][i]
            result = "Case #%d: %s won" % (index+1, c)
            break
    if result:
        print result
    else:
        if may_draw:
            print "Case #%d: Draw" % (index+1,)
        else:
            print "Case #%d: Game has not completed" % (index+1,)
    index += 1
