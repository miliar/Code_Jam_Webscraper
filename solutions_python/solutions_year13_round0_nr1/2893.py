#!/usr/bin/python

def solve_tic_tac_toe(board):
    not_finished = 0
    for i in xrange(4):
        if board[i][0] != 'T':
            player = board[i][0]
        else:
            player = board[i][1]
        for j in xrange(1, 4):
            if board[i][j] == '.':
                not_finished = 1
                break
            else:
                if board[i][j] != player:
                    if board[i][j] != 'T':
                        break
                if j == 3:
                    return '%s won' %(player)

    for j in xrange(4):
        if board[0][j] != 'T':
            player = board[0][j]
        else:
            player = board[1][j]
        for i in xrange(1, 4):
            if board[i][j] == '.':
                not_finished = 1
                break
            else:
                if board[i][j] != player:
                    if board[i][j] != 'T':
                        break
                if i == 3:
                    return '%s won' %(player)

    player = board[0][0]
    for i in xrange(1, 4):
        if board[i][i] == '.':
            not_finished = 1
            break
        else:
            if board[i][i] != player:
                if board [i][i] != 'T':
                    break
            if i == 3:
                return '%s won' %(player)

    player = board[0][3]
    for i in xrange(1, 4):
        if board[i][3-i] == '.':
            not_finished = 1
            break
        else:
            if board[i][3-i] != player:
                if board[i][3-i] != 'T':
                    break
            if i == 3:
                return '%s won' %(player)
    if not_finished:
        return 'Game has not completed'
    return 'Draw'
    
                
    
def main():
    f = open("A-small-attempt1.in")
    output = testcases = open("A-small-attempt1.out", 'w')
    N = int(f.readline())
    for i in xrange(N):
        board = []
        for j in xrange(4):
            board.append(f.readline())
        output.write('Case #%d: ' % (i + 1) + solve_tic_tac_toe(board))
        output.write('\n')
        f.readline()
    output.close()

if __name__ == '__main__':
	main()
