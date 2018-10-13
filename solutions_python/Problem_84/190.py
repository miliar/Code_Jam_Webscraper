from sys import stdin

def input():
    n = int(stdin.next())
    cases = []
    for i in range(n):
        R, C = stdin.next().split()
        R = int(R)
        C = int(C)
        m = []
        for j in range(R):
            l = stdin.next().strip()
            l = list(l)
            m.append(l)
        cases.append(m)
    return cases 

def try_it(case):
    R = len(case)
    C = len(case[0])
    for i in range(R):
        for j in range(C):
            if case[i][j] == '#':
                fill(case, i, j)

def fill(case, x, y):
    R = len(case)
    C = len(case[0])
    if (x + 1 < R) and (y + 1 < C):
        if case[x][y] != '#' or \
                case[x][y + 1] != '#' or \
                case[x + 1][y] != '#' or \
                case[x + 1][y + 1] != '#':
                    return
        case[x][y] = '/'
        case[x][y + 1] = '\\'
        case[x + 1][y] = '\\'
        case[x + 1][y + 1] = '/'

def check(case):
    for x in case:
        if '#' in x:
            return False
    return True

def output(case):
    for x in case:
        print ''.join(x)

def main():
    cases = input()
    for index, case in enumerate(cases):
        print 'Case #%d:' % (index + 1)
        try_it(case)
        if check(case):
            output(case)
        else:
            print 'Impossible'

main()
    
    
