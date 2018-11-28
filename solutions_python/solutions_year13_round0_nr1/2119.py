import sys

def isWin(l, p):
    for a in l:
        if a != p and a != 'T':
            return False
    return True

def solve(t):
    board = []
    dia1, dia2 = [], []
    for i in xrange(0, 4):
        line = raw_input()
        board.append(line)
        dia1.append(line[i])
        dia2.append(line[3-i])
    raw_input()

    for l in board:
        if isWin(l, 'X'):
            end = True
            print 'Case #%d:'%t, 'X won'
            return
        elif isWin(l, 'O'):
            end = True
            print 'Case #%d:'%t, 'O won'
            return

    board = zip(*board)
    for l in board:
        if isWin(l, 'X'):
            print 'Case #%d:'%t, 'X won'
            return
        elif isWin(l, 'O'):
            print 'Case #%d:'%t, 'O won'
            return

    if isWin(dia1, 'X') or isWin(dia2, 'X'):
        print 'Case #%d:'%t, 'X won'
        return
    elif isWin(dia1, 'O') or isWin(dia2, 'O'):
        print 'Case #%d:'%t, 'O won'
        return

    for l in board:
        for a in l:
            if a == '.':
                print 'Case #%d:'%t, 'Game has not completed'
                return

    print 'Case #%d:'%t, 'Draw'

def main():
    sys.stdin = open('A-large.in')
    f = file('A-large.out', 'w')
    f.close()
    sys.stdout = open('A-large.out', 'w')

    T = input()
    for t in xrange(1, T+1):
        solve(t)


if __name__ == '__main__':
    main()
