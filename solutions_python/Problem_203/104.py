cases = int(input())
for case in range(1, cases+1):
    r, c = map(int, input().split(' '))
    board = []
    fix_first = False
    for r_num in range(r):
        row = list(input())
        letters = set(row)
        if '?' not in letters:
            #row is full, we're done
            board.append(row)
        elif len(letters) > 1:
            #there's at least 1 letter in the row
            current_letter = [x for x in row if x != '?'][0]
            for i in range(c):
                if row[i] == '?':
                    row[i] = current_letter
                else:
                    current_letter = row[i]
            board.append(row)
        else:
            #row is all ?s
            if r_num == 0:
                fix_first = True
                board.append(row)
            else:
                board.append(board[r_num - 1])

    if fix_first:
        first_good = [x for x in board if '?' not in x][0]
        for i in range(r):
            if '?' in board[i]:
                board[i] = first_good
            else:
                break

    print("Case #{}:".format(case))
    for i in board:
        print(''.join(i))
