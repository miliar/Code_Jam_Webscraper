VECTORS = [(0, 1), (1, 1), (1, 0), (1, -1)]
N = 4
X = 'X'
O = 'O'
T = 'T'

for t in range(input()):
    print "Case #%s:" % str(t + 1),
    board = [raw_input() for i in range(N)]
    ended = True
    for i in range(N):
        j = 0
        if board[i][j] == 'T':
            j += 1
        player = board[i][j]
        if player == '.':
            ended = False
        else:
            try:
                while board[i][j] == player or board[i][j] == T:
                    j += 1
                if board[i][j] == '.':
                    ended = False
            except IndexError:
                print player + " won"
                break
        j = 0
        if board[j][i] == 'T':
            j += 1
        player = board[j][i]
        if player == '.':
            ended = False
            continue
        try:
            while board[j][i] == player or board[j][i] == T:
                j += 1
            if board[j][i] == '.':
                ended = False
        except IndexError:
            print player + " won"
            break
    else:
        j = 0
        i = 0
        if board[i][j] == 'T':
            j += 1
            i += 1
        player = board[i][j]
        if player == '.':
            ended = False
        else:
            try:
                while board[i][j] == player or board[i][j] == T:
                    i += 1
                    j += 1
                if board[i][j] == '.':
                    ended = False
            except IndexError:
                print player + " won"
                raw_input()
                continue
        j =  - 1
        i = 0
        if board[i][j] == 'T':
            j -= 1
            i += 1
        player = board[i][j]
        if player == '.':
            ended = False
        else:
            try:
                while board[i][j] == player or board[i][j] == T:
                    i += 1
                    j -= 1
                if board[i][j] == '.':
                    ended = False
            except IndexError:
                print player + " won"
                raw_input()
                continue
        if ended:
            print "Draw"
        else:
            print "Game has not completed"
    raw_input()
