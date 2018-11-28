import sys

'''
x - 0
o - 1
draw - 2
no - 3
'''

def same(a, b, c, d):
    l = [a,b,c,d]
    ch = ''
    for i in l:
        if i != 'T':
            ch = i
            break
    for i in range(4):
        if l[i] == 'T':
            l[i] = ch
    res = -1
    if (ch == 'X'): res = 0
    if (ch == 'O'): res = 1
    if l[0] == l[1] == l[2] == l[3] == ch:
        return res
    return -1

def draw(l):
    full = True
    for i in l:
        if full is False: break
        for j in i:
            if j == '.':
                full = False
                break
    return full

def judge(l):
    for i in range(4):
        res = same(l[0][i], l[1][i], l[2][i], l[3][i])
        if res == 0:
            return "X won"
        if res == 1:
            return "O won"

        res = same(l[i][0], l[i][1], l[i][2], l[i][3])
        if res == 0:
            return "X won"
        if res == 1:
            return "O won"

    res = same(l[0][0], l[1][1], l[2][2], l[3][3])
    if res == 0:
        return 'X won'
    if res == 1:
        return 'O won'

    res = same(l[0][3], l[1][2], l[2][1], l[3][0])
    if res == 0:
        return 'X won'
    if res == 1:
        return 'O won'

    if draw(l):
        return "Draw"
    
    return "Game has not completed"

def main():
    data = sys.stdin.readlines()
    num = int(data[0])
    index = 1;
    for i in range(1, num+1):
        l = [data[m].strip() for m in range(index, index+4)]
        index += 5
        res = judge(l)
        print 'Case #%d: %s' % (i, res)
main()
