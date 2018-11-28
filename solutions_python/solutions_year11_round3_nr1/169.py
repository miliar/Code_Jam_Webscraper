import sys

cin = sys.stdin
cases = int(cin.next()) # skip line saying number of cases


for case in range(cases):
    print("Case #%d:" % (case+1,))
    r, c = map(int, cin.next().strip().split())
    board = []
    for i in range(r):
        board.append(list(cin.next().strip()))

    possible = True
    try:
        for rr in range(r):
            for cc in range(c):
                if board[rr][cc] == '#':
                    board[rr][cc] = '/'
                    if board[rr][cc+1] != '#':
                        possible = False
                    else:
                        board[rr][cc+1] = '\\'
                    if board[rr+1][cc] != '#':
                        possible = False
                    else:
                        board[rr+1][cc] = '\\'
                    if board[rr+1][cc+1] != '#':
                        possible = False
                    else:
                        board[rr+1][cc+1] = '/'
    except Exception as ex:
        possible = False

    if possible:
        print("\n".join([''.join(x) for x in board]))
    else:
        print("Impossible")



