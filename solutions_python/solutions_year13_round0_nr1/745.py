def check_row(row):
    num_o = 0
    num_t = 0
    num_x = 0
    num_empty = 0
    for c in row:
        if c == 'O':
            num_o += 1
        elif c == 'T':
            num_t += 1
        elif c == 'X':
            num_x += 1
        elif c == '.':
            num_empty += 1
    if num_t > 0:
        num_o += 1
        num_x += 1
    return num_o == 4, num_x == 4, num_empty > 0


if __name__ == '__main__':
    infile = open('data.in', 'rb')
    num_cases = int(infile.readline())
    for case_num in range(1, num_cases + 1):
        # load up the board rows
        rows = []
        for row_num in range(4):
            row = infile.readline().strip()
            rows.append(row)
        # augment rows with columns and diagonals
        cols = []
        for col_num in range(4):
            row = ''
            for row_num in range(4):
                row += rows[row_num][col_num]
            cols.append(row)
        for start, dir in (0, 1), (3, -1):
            row = ''
            for row_num in range(4):
                row += rows[row_num][start + dir * row_num]
            cols.append(row)
        rows.extend(cols)

        o_won = x_won = moves_remaining = False
        for row in rows:
            o_wins, x_wins, empty_cells = check_row(row)
            o_won |= o_wins
            x_won |= x_wins
            moves_remaining |= empty_cells
        
        if o_won and x_won or (not (o_won or x_won) and not moves_remaining):
            result = 'Draw'
        elif o_won:
            result = 'O won'
        elif x_won:
            result = 'X won'
        else:
            result = 'Game has not completed'
        print 'Case #%d: %s' % (case_num, result)
        infile.readline() # consume blank