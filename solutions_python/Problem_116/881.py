def solve(case_id, game_board, out):
    not_completed = False
    #check rows:
    for line in game_board:
        winner = ' '
        for el in line:
            if el == '.':
                not_completed = True
                break
            elif winner == ' ' and el != 'T':
                winner = el
            elif winner != ' ' and el != 'T' and el != winner:
                break
        else:
            out.write("Case #" + str(case_id) + ": " + winner + " won\n")
            return

    #check columns:
    for col in range(0,4):
        winner = ' '
        for line in range(0,4):
            el = game_board[line][col]
            if el == '.':
                not_completed = True
                break
            elif winner == ' ' and el != 'T':
                winner = el
            elif winner != ' ' and el != 'T' and el != winner:
                break
        else:
            out.write("Case #" + str(case_id) + ": " + winner + " won\n")
            return

    #check diagonals:
    winner = ' '
    for i in range(0,4):
        el = game_board[i][i]
        if el == '.':
            not_completed = True
            break
        elif winner == ' ' and el != 'T':
            winner = el
        elif winner != ' ' and el != 'T' and el != winner:
            break
    else:
        out.write("Case #" + str(case_id) + ": " + winner + " won\n")
        return
        
    winner = ' '
    for i in range(0,4):
        el = game_board[i][4 - i - 1]
        if el == '.':
            not_completed = True
            break
        elif winner == ' ' and el != 'T':
            winner = el
        elif winner != ' ' and el != 'T' and el != winner:
            break
    else:
        out.write("Case #" + str(case_id) + ": " + winner + " won\n")
        return
    if not_completed:
        out.write("Case #" + str(case_id) + ": Game has not completed\n")
    else:
        out.write("Case #" + str(case_id) + ": Draw\n")



input_file = 'A-large.in'
output_file = 'output.txt'

f = open(input_file, 'r')
out = open(output_file, 'w')

#read no test cases:
no_tests = int(f.readline())

for test in range(0, no_tests):
    #read board game state:
    game_board = []
    for line in f:
        if line == '\n':
            break
        line = line.strip()
        row = []
        for i in range(0, len(line)):
            row.append(line[i])
        game_board.append(row)
    solve(test+1, game_board, out)
    
f.close()
out.close()
