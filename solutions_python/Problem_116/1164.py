lines = 0

def chartoint(char):
    if char == '.':
        return 0
    elif char == 'T':
        return 1
    elif char == 'X':
        return 2
    elif char == 'O':
        return 3
    else:
        return 1

combos = [[(i, i2) for i in range(4)] for i2 in range(4)] + [[(i2, i) for i in range(4)] for i2 in range(4)] + [[(i,i) for i in range(4)]] + [[(i, 3-i) for i in range(4)]]
            

def decide_gamestate(board):
    nboard = [[None, None, None, None],[None, None, None, None],[None, None, None, None],[None, None, None, None]]
    for i in range(4):
        for i2 in range(4):
            nboard[i][i2] = chartoint(board[i][i2])
    for i in range(len(combos)):
        product = 1
        for i2 in range(4):
            product *= nboard[combos[i][i2][0]][combos[i][i2][1]]
        if (product != 0) & (product % 2 == 0) & (product % 3 != 0):
            return 'X'
        elif (product != 0) & (product % 3 == 0) & (product % 2 != 0):
            return 'O'
    product = 1
    for i in range(4):
        for i2 in range(4):
            product *= nboard[i][i2]
    if product == 0:
        return 'G'
    else:
        return 'D'


def parse():
    f = open('tttt_large.txt', 'r+')
    games = int(f.readline())
    for i in range(games):
        board = []
        for i2 in range(4):
            board.append(f.readline())
        f.readline()
        res = decide_gamestate(board)
        if res == 'X':
            res = "X won"
        elif res == 'O':
            res = "O won"
        elif res == 'D':
            res = "Draw"
        elif res == 'G':
            res = "Game has not completed"
        else:
            res = "Error " + res
        print("Case #" + str(i+1) + ": " + res)

parse()
