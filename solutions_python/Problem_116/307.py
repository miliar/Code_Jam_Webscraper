from itertools import chain

mosse = list(chain(
    [[(i,j) for i in range(4)] for j in range(4)],
    [[(i,j) for j in range(4)] for i in range(4)],
    [[(i,i) for i in range(4)]],
    [[(i,3-i) for i in range(4)]]))

n = int(input())

for k in range(1, n+1):
    board = [input() for i in range(4)]

    if any(all(board[i][j] in ('X', 'T') for i, j in m) for m in mosse):
        print("Case #%d: X won" % k)
    elif any(all(board[i][j] in ('O', 'T') for i, j in m) for m in mosse):
        print("Case #%d: O won" % k)
    elif all(board[i][j] != '.' for i in range(4) for j in range(4)):
        print("Case #%d: Draw" % k)
    else:
        print("Case #%d: Game has not completed" % k)

    input()
