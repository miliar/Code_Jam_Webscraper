in_put = open("input.in", 'r')
output = open("output.out", 'w')

BOARD_SIZE = 4

test_count = int(in_put.next())

for test in range(1, test_count + 1):
    if test > 1:
        output.write("\n")
    winner = True
    board = []
    moves_possible = False
    for i in range(0, BOARD_SIZE):
        curr_text_line = in_put.next()
        if curr_text_line == "\n":
            curr_text_line = in_put.next()
            
        board.append([])
        if curr_text_line.find(".") > -1:
            moves_possible = True
        
        for j in range(0, BOARD_SIZE):
            board[i].append(curr_text_line[j])
    
    # check for winning pattern in all rows
    for i in range(0, BOARD_SIZE):
        winner = True
        winning_symbol = board[i][0]
        if winning_symbol == "T":
            winning_symbol = board[i][1]
        if winning_symbol == ".":
            # can't be a winner
            winner = False
            continue
        
        for j in range(1, BOARD_SIZE):
            if board[i][j] == winning_symbol or board[i][j] == "T":
                continue
            else:
                winner = False
                break
        
        if winner:
            output.write("Case #" + str(test) + ": " + winning_symbol + " won")
            break
    
    if winner:
        continue # next test
    
    # check for winning pattern in all columns
    for i in range(0, BOARD_SIZE):
        winner = True
        winning_symbol = board[0][i]
        if winning_symbol == "T":
            winning_symbol = board[1][i]
        if winning_symbol == ".":
            # can't be a winner
            winner = False
            continue
        
        for j in range(1, BOARD_SIZE):
            if board[j][i] == winning_symbol or board[j][i] == "T":
                continue
            else:
                winner = False
                break
        
        if winner:
            output.write("Case #" + str(test) + ": " + winning_symbol + " won")
            break
        
    if winner:
        continue # next test
        
    # check diagonal from top left to bottom right
    winner = True
    winning_symbol = board[0][0]
    if winning_symbol == "T":
        winning_symbol = board[1][1]
    if winning_symbol == ".":
        # can't be a winner
        winner = False

    if winner:
        for i in range(1, BOARD_SIZE):
            if board[i][i] == winning_symbol or board[i][i] == "T":
                continue
            else:
                winner = False
                break
        
    if winner:
        output.write("Case #" + str(test) + ": " + winning_symbol + " won")
        continue # next test
        
    # check diagonal from top right to bottom left
    winner = True
    winning_symbol = board[0][BOARD_SIZE - 1]
    if winning_symbol == "T":
        winning_symbol = board[1][BOARD_SIZE - 2]
    if winning_symbol == ".":
        # can't be a winner
        winner = False

    if winner:
        for i in range(1, BOARD_SIZE):
            if board[i][BOARD_SIZE - i - 1] == winning_symbol or board[i][BOARD_SIZE - i - 1] == "T":
                continue
            else:
                winner = False
                break
        
    if winner:
        output.write("Case #" + str(test) + ": " + winning_symbol + " won")
        continue # next test
    
    # no winner, see if game not completed or draw
    if moves_possible:
        output.write("Case #" + str(test) + ": Game has not completed")
    else:
        output.write("Case #" + str(test) + ": Draw")