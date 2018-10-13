import sys

def all_same(items):
    return (all(x == items[0] for x in items), items[0])

def check_win(items):
    x_count = 0
    o_count = 0
    e_count = 0
    for c in items:
        if c == 'X':
            x_count += 1
        elif c == 'O':
            o_count += 1
        elif c == 'T':
            x_count += 1
            o_count += 1
        # '.' character
        elif c == '.':
            e_count += 1
        else:
            return (False, '.', e_count)
    if x_count == 4:
        return (True, 'X', e_count)

    if o_count == 4:
        return (True, 'O', e_count)

    return (False, '.', e_count)


if __name__ == "__main__":
    file_name = str(sys.argv[1])
    f = open (file_name, "r")

    # Step 1 - Read the number of datasets and set counter for data
    N = int(f.readline())
    counter = 0

    output_file = open("tcitactoe.out", "w")

    # Iterate through all data
    
    while counter < N:
        has_winner = False
        counter += 1
        output_line = "Case #" + str(counter) + ": "
        # reads the baord into 4 x 4 matrix
        board = []
        e_count = 0
        for _ in range(4):
            line = (f.readline()).strip('\n')
            board.append(list(line))
        for i in range(4):
            # check horizontal line
            hline = board[i]
            (win, winner, e) = check_win(board[i])
            e_count += e
            if win == True:
                output_line += winner + ' won'
                has_winner = True
                break  
            # check vertical line
            vline = [board[j][i] for j in range(4)]
            (win, winner, e) = check_win(vline)
            e_count += e
            if win == True:
                output_line += winner + ' won'
                has_winner = True
                break
            
        # check left diagonal lines
        ldline = [board[j][j] for j in range(4)]
        (win, winner, e) = check_win(ldline)
        e_count += e
        if win == True:
            output_line += winner + ' won'
            has_winner = True

        # check right diagonal lines
        rdline = [board[j][3-j] for j in range(4)]
        (win, winner, e) = check_win(rdline)
        e_count += e
        if win == True:
            output_line += winner + ' won'
            has_winner = True

        if (e_count == 0) & (has_winner== False):
            output_line += 'Draw'
        if (e_count > 0) & (has_winner == False):
            output_line += 'Game has not completed'

        f.readline()
        print(output_line)
        output_file.write(output_line + "\n")

    f.close()
    output_file.close()
