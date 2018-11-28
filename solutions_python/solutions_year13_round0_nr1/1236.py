def check(s):
    if s.count('O') + s.count('T') == 4:
        return 'O'
    if s.count('X') + s.count('T') == 4:
        return 'X'
    return '$'


def main():
    fin = open('a.in', 'r')
    fout = open('a.out', 'w')
    t = int(fin.readline())

    for c in xrange(t):
        board = []
        dot = False
        for i in range(4):
            board.append(fin.readline().strip().strip('\n'))
            if board[i].find('.') != -1:
                dot = True

        fin.readline()

        xwin = owin = False
        for i in range(4):
            status = check(''.join(board[i]))
            if status == 'X':
                xwin = True
                break
            elif status == 'O':
                owin = True
                break
        for j in range(4):
            status = check(board[0][j]+board[1][j]+board[2][j]+board[3][j])
            if status == 'X':
                xwin = True
                break
            elif status == 'O':
                owin = True
                break

        status = check(board[0][0]+board[1][1]+board[2][2]+board[3][3])
        if status == 'X':
            xwin = True
        elif status == 'O':
            owin = True

        status = check(board[0][3]+board[1][2]+board[2][1]+board[3][0])
        if status == 'X':
            xwin = True
        elif status == 'O':
            owin = True

        fout.write('Case #%d: ' % (c+1))
        if (xwin and owin) or (not dot and not xwin and not owin):
            fout.write('Draw\n')
        elif (xwin and not owin):
            fout.write('X won\n')
        elif (owin and not xwin):
            fout.write('O won\n')
        else:
            fout.write('Game has not completed\n')

    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
