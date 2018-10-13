def if_win(board, c):
    for ri in xrange(4):
        win = True
        for ci in xrange(4):
            if board[ri][ci] != c and board[ri][ci] != 'T':
                win = False
                break
        if win: return True
    for ci in xrange(4):
        win = True
        for ri in xrange(4):
            if board[ri][ci] != c and board[ri][ci] != 'T':
                win = False
                break
        if win: return True
    win = True
    for di in xrange(4):
        if board[di][di] != c and board[di][di] != 'T':
            win = False
            break
    if win: return True
    win = True
    for di in xrange(4):
        if board[3-di][di] != c and board[3-di][di] != 'T':
            win = False
            break
    if win: return True
    return False

def main():
    T = int(raw_input())
    for ti in xrange(T):
        print "Case #{0}:".format(ti+1),
        board = [raw_input() for i in xrange(4)]
        try:
            raw_input()
        except EOFError:
            pass

        if if_win(board, 'X'):
            print "X won"
        elif if_win(board, 'O'):
            print "O won"
        else:
            draw = True
            for ri in range(4):
                for ci in range(4):
                    if board[ri][ci] == '.':
                        draw = False
                        break
            if draw:
                print "Draw"
            else:
                print "Game has not completed"

    pass

if __name__ == "__main__":
    main()
