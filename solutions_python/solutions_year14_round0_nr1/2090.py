cases = int(raw_input())

for case in range(1, cases+1):
    row_index = int(raw_input()) - 1

    board = []
    for rows in range(4):
        board += [raw_input().split(' ')]

    first_row = set(board[row_index])

    row_index = int(raw_input()) - 1

    board = []
    for rows in range(4):
        board += [raw_input().split(' ')]

    second_row = set(board[row_index])

    intersection = list(first_row & second_row)

    if len(intersection) == 1:
        print "Case #{0}: {1}".format(case, intersection[0])
    elif len(intersection) > 1:
        print "Case #{0}: Bad magician!".format(case)
    else:
        print "Case #{0}: Volunteer cheated!".format(case)




