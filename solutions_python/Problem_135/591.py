import sys

for tc in range(1, int(sys.stdin.readline()) + 1):
    first = int(sys.stdin.readline()) - 1
    board = [[] for _ in range(4)]
    for i in range(4):
        board[i] = [int(x) for x in sys.stdin.readline().split()]
    
    second = int(sys.stdin.readline()) - 1
    second_board = [[] for _ in range(4)]
    for i in range(4):
        second_board[i] = [int(x) for x in sys.stdin.readline().split()]

    row = set(board[first]).intersection(second_board[second])

    if len(row) == 1:
        print("Case #{}: {}".format(tc, list(row)[0]))
    elif len(row) > 1:
        print("Case #{}: {}".format(tc, "Bad magician!"))
    else:
        print("Case #{}: {}".format(tc, "Volunteer cheated!"))

