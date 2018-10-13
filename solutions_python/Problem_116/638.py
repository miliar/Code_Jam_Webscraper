fin = open("in", "r")
fout = open("out", "w")

T = fin.readline()
T = int(T.strip())

for i in range(0, T):
    board = []
    num_empty = 0
    j = 0
    while j < 4:
        inpt = (fin.readline()).strip()
        if inpt != '':
            board.append(inpt)
            j += 1      

    # rows
    for row in board:
        start = 1
        first = row[0]
        cnt = 1
        if first == 'T':
            first = row[1]
            start = 2
            cnt = 2
        if first == '.':
            num_empty += 1
            continue
        for j in range(start, 4):
            if row[j] == first or row[j] == 'T':
                cnt += 1
            else:
                if row[j] == '.':
                    num_empty += 1
                break
        if cnt == 4:
            fout.write("Case #%d: %s won\n" %(i+1, first))
            break

    if cnt == 4: continue

    # cols
    for j in range(0, 4):
        start = 0
        first = board[0][j]
        if first == 'T':
            first = board[1][j]
            start = 2
        if first == '.':
            continue
        cnt = 0
        for k in range(start, 4):
            if board[k][j] == first or board[k][j] == 'T':
                cnt += 1
            else:
                break

        if cnt == 4:
            fout.write("Case #%d: %s won\n" %(i+1, first))
            break

    if cnt == 4:
        continue

    # diagonals
    cnt = 1
    start = 1
    first = board[0][0]
    if first == 'T':
        first = board[1][1]
        start = 2
    if first != '.':
        for j in range(start, 4):
            if first == board[j][j] or board[j][j] == 'T':
                cnt += 1
            else:
                break

    if cnt == 4:
        fout.write("Case #%d: %s won\n" %(i+1, first))
        continue

    cnt = 1
    start = 1
    first = board[0][3]
    if first == 'T':
        first = board[1][2]
        start = 2
    if first != '.':
        for j in range(start, 4):
            if first == board[j][3-j] or board[j][3-j] == 'T':
                cnt += 1
            else:
                break

    if cnt == 4:
        fout.write("Case #%d: %s won\n" %(i+1, first))
        continue

    if num_empty > 0:
        fout.write("Case #%d: Game has not completed\n" %(i+1))
    else:
        fout.write("Case #%d: Draw\n" %(i+1))


fin.close()
fout.close()