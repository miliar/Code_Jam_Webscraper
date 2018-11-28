import linecache

cases = 10
lines = 49
filename = 'small.in'

case = 1
txtline = 1
while case <= cases and txtline <= lines:
    line0 = linecache.getline(filename, txtline)
    line1 = linecache.getline(filename, txtline+1)
    line2 = linecache.getline(filename, txtline+2)
    line3 = linecache.getline(filename, txtline+3)
    board_horizontal = [line0, line1, line2, line3]

    # Board from a vertical point of view
    line0 = line1 = line2 = line3 = ''
    for line in board_horizontal:
        line0 += line[0]
        line1 += line[1]
        line2 += line[2]
        line3 += line[3]
    board_vertical = [line0, line1, line2, line3]
    #print(board2)
    
    # Diagonal
    line1_index = 0
    line2_index = 3
    line1 = line2 = ''
    for line in board_horizontal:
        line1 = line1 + line[line1_index]
        line2 = line2 + line[line2_index]
        line1_index += 1
        line2_index -= 1
    board_diagonal = [line1, line2]
    
    board = board_horizontal + board_vertical + board_diagonal
    #print(board)
    
    # Check if there is a winner
    result = ''
    someone_won = False
    empty_square = False
    for line in board:
        #print(line)
        if 'XXXT' in line or 'XXXX' in line:
            result = 'X won'
            someone_won = True
            break
        if 'OOOT' in line or 'OOOO' in line:
            result = 'O won'
            someone_won = True
            break
        if '.' in line:
            empty_square = True
    
    if not someone_won:
        if empty_square:
            result = 'Game has not completed'
        else:
            result = 'Draw'
    
    
    print('Case #{}: {}'.format(case, result))
    case = case + 1
    txtline = txtline + 5
