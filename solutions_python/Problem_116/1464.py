import fileinput

def isO(ch):
    return ch == 'O' or ch == 'T'
def isX(ch):
    return ch == 'X' or ch == 'T'

def isBingo(s):
    if isO(s[0]) and isO(s[1]) and isO(s[2]) and isO(s[3]):
        return 'O'
    elif isX(s[0]) and isX(s[1]) and isX(s[2]) and isX(s[3]):
        return 'X'
    else:
        return '.'

def notCompleted(m):
    for line in m:
        for ang in line:
            if ang is '.':
                return True
    return False
def findBingo(m):
    for i in range(4):
        if isBingo(m[i]) is not '.':
            return isBingo(m[i])
    for i in range(4):
        tmp = [ m[0][i], m[1][i], m[2][i], m[3][i] ]
        if isBingo(tmp) is not '.':
            return isBingo(tmp)
    diag1 = [ m[0][0], m[1][1], m[2][2], m[3][3] ]
    diag2 = [ m[0][3], m[1][2], m[2][1], m[3][0] ]
    if isBingo(diag1) is not '.':
        return isBingo(diag1)
    if isBingo(diag2) is not '.':
        return isBingo(diag2)
    if notCompleted(m):
        return 'n'
    return '.'

def solve():
    inf = open('ang')
    content = inf.readlines()
    inf.close()

    outf = open('out', 'w')

    T = int(content[0])
    for i in range(T):
        n = i + 1
        m = [ content[1 + i * 5], content[2 + i * 5], content[3 + i * 5], content[4 + i * 5] ]
        r = findBingo(m)
        if r is 'O':
            outf.write('Case #%d: O won\n'%n)
        elif r is 'X':
            outf.write('Case #%d: X won\n'%n)
        elif r is 'n':
            outf.write('Case #%d: Game has not completed\n'%n)
        elif r is '.':
            outf.write('Case #%d: Draw\n'%n)
    outf.close()
