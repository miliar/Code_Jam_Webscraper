def check(board, pos_x, pos_y, inc_x, inc_y):
    ch = board[pos_x][pos_y]

    cnt = 3

    cur_x = pos_x + inc_x
    cur_y = pos_y + inc_y

    while (cur_x >= 0 and cur_x < 4 and cur_y >= 0 and cur_y < 4):
        #print(cur_x, cur_y)
        cur_ch = board[cur_x][cur_y]
        if (cur_ch == 'T' or cur_ch == ch):
            cur_x = cur_x + inc_x
            cur_y = cur_y + inc_y
            cnt -= 1
        else:
            break

    cur_x = pos_x - inc_x
    cur_y = pos_y - inc_y

    while (cur_x >= 0 and cur_x < 4 and cur_y >= 0 and cur_y < 4):
        #print(cur_x, cur_y)
        cur_ch = board[cur_x][cur_y]
        if (cur_ch == 'T' or cur_ch == ch):
            cur_x = cur_x - inc_x
            cur_y = cur_y - inc_y
            cnt -= 1
        else:
            break

    return cnt == 0


def check_horiz(board, pos_x, pos_y):
    return check(board, pos_x, pos_y, 0, 1)

def check_vert(board, pos_x, pos_y):
    return check(board, pos_x, pos_y, 1, 0)

def check_diag_1(board, pos_x, pos_y):
    return check(board, pos_x, pos_y, 1, 1)

def check_diag_2(board, pos_x, pos_y):
    return check(board, pos_x, pos_y, 1, -1)

def check_winner(board):
    is_done = True
    #print(board)

    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == ".":
                is_done = False
            if board[i][j] != "." and board[i][j] != "T":
                res = check_horiz(board,i,j) or check_vert(board,i,j) or check_diag_1(board,i,j) or check_diag_2(board,i,j)
                if res:
                    return board[i][j] + " won"

    if is_done:
        return "Draw"
    else:
        return "Game has not completed"


if __name__ == "__main__":
    testcases = int(input())

    for caseNr in range(0, testcases):
        l1 = input()
        l2 = input()
        l3 = input()
        l4 = input()
        input()

        print("Case #%i: %s" % (caseNr+1, check_winner([l1,l2,l3,l4])))
