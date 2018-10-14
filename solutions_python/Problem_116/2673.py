def get_empty_board():
    return ([], [], [], [])

def process_board(board, iteration):
    cols = [[], [], [], []]

    #check horizontal
    match_right_diagnol = {}
    match_left_diagnol = {}
    farthest = 3
    closest = 0
    complete = True
    for row in board:
        if ("X" in row or "T" in row) and "O" not in row and "." not in row:
            return "Case #%d: X won" % (iteration)
        elif ("O" in row or "T" in row) and "X" not in row and "." not in row:
            return "Case #%d: O won" % (iteration)

        if "." in row:
            complete = False

        count = 0
        for letter in row:
            if count == 4:
                continue
            if count == farthest:
                match_right_diagnol[farthest] = letter
            if count == closest:
                match_left_diagnol[closest] = letter
            cols[count].append(letter)
            count=count+1

        closest = closest + 1 
        farthest = farthest - 1

    diagnol1 = match_left_diagnol.values()
    diagnol2 = match_right_diagnol.values()
    if ("X" in diagnol1 or "T" in diagnol1) and "O" not in diagnol1 and "." not in diagnol1:
        return "Case #%d: X won" % (iteration)
    elif ("O" in diagnol1 or "T" in diagnol1) and "X" not in diagnol1 and "." not in diagnol1:
        return "Case #%d: O won" % (iteration)

    if ("X" in diagnol2 or "T" in diagnol2) and "O" not in diagnol2 and "." not in diagnol2:
        return "Case #%d: X won" % (iteration)
    elif ("O" in diagnol2 or "T" in diagnol2) and "X" not in diagnol2 and "." not in diagnol2:
        return "Case #%d: O won" % (iteration)

    #check vertical
    for col in cols:
        if ("X" in col or "T" in col) and "O" not in col and "." not in col:
            return "Case #%d: X won" % (iteration)
        elif ("O" in col or "T" in col) and "X" not in col and "." not in col:
            return "Case #%d: O won" % (iteration)

    if complete:
        return "Case #%d: Draw" % iteration
    else:
        return "Case #%d: Game has not completed" % (iteration)
        






iteration = 1
with open('/home/tipu/Downloads/A-large.in', 'r') as f:
    input_size = None
    row = 0
    for line in f.readlines():
        if input_size == None:
            input_size = int(line)
            board = get_empty_board()
            row = 0
            continue
        if row == 4:
            print(process_board(board, iteration))
            board = get_empty_board()
            row = 0
            iteration = iteration + 1
            continue
        for piece in line:
            board[row].append(piece)
        row = row + 1

