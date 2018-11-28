import sys

name = "D-small"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

T = int(input())

for test_case in range(T):
    N, M = (int(x) for x in input().split())
    forbidden = -1
    top_row = ['.'] * N
    add_tuples = []

    for i in range(M):
        model, row, column = input().split()
        row = int(row) - 1
        column = int(column) - 1
        top_row[column] = model
        if model != '+':
            forbidden = column

    for x, val in enumerate(top_row):
        if x == N - 1 and forbidden == -1:
            forbidden = x
            add_tuples.append(('o', 1, x + 1))
            break
        if val == '.':
            add_tuples.append(('+', 1, x + 1))
        if val == 'x':
            add_tuples.append(('o', 1, x + 1))

    last_diag = None
    start_x = forbidden + 1 if forbidden + 1 != N else 0
    start_y = 1
    while start_y < N:
        if start_y == N-1:
            if start_x != 0 and start_x != N-1:
                add_tuples.append(('o', start_y + 1, start_x + 1))
            else:
                add_tuples.append(('x', start_y + 1, start_x + 1))
            last_diag = start_x
            break
        add_tuples.append(('x', start_y + 1, start_x + 1))
        start_y += 1
        start_x += 1
        if start_x == N:
            start_x = 0

    for x in range(1, N-1):
        if x != last_diag:
            add_tuples.append(('+', N, x + 1))

    points = 3*N - 2 if N > 1 else 2
    print("Case #" + str(test_case + 1) + ": %d %d" % (points, len(add_tuples)))
    for tup in add_tuples:
        print("%s %d %d" % tup)