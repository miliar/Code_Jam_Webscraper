from sets import Set

def matrix(f):
    a = []
    for i in range(0, 4):
        a.append(f.readline().strip())
    return a

def check(a, b, c, d):
    s = Set([a, b, c, d])
    if len(s) >= 3:
        if '.' in s:
            return '.'
        else:
            return ''
    else:
        if len(s) == 2:
            if 'T' in s:
                s.remove('T')
                return s.pop()
            else: 
                return ''
        else:
            return s.pop()
    
def init():
    w = open('ou.txt', 'w')
    f = open('A-large.in', 'r')
    num = int(f.readline())
    for i in range(1, num + 1):
        w.write('Case #' + str(i) + ': ')
        m = matrix(f)
        x = ''
        for j in range(0, 4):
            x = x + check(m[j][0], m[j][1], m[j][2], m[j][3])
            x = x + check(m[0][j], m[1][j], m[2][j], m[3][j])
        x = x + check(m[0][0], m[1][1], m[2][2], m[3][3])
        x = x + check(m[0][3], m[1][2], m[2][1], m[3][0])
        if len(x) == 0:
            w.write('Draw\n')
        else:
            if '.' in x:
                x = x.replace('.', '')
                if len(x) == 0:
                    w.write('Game has not completed\n')
                else:
                    w.write(x[0] + ' won\n')
            else:
                w.write(x[0] + ' won\n')
        f.readline()
    w.close()
    f.close()

if __name__ == '__main__':
    init()
