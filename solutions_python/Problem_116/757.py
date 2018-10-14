T = 'T'
X = 'X'
O = 'O'
Blank = '.'

f = open('G:/Study/Programming/Code Jam/2013/A-large.in', 'r')
#f = open('G:/Study/Programming/Code Jam/trial.txt', 'r')
g = open('G:/Study/Programming/Code Jam/2013/output1_large.txt', 'w')
#g = open('G:/Study/Programming/Code Jam/output_trial.txt', 'w')
no_test_cases = int(f.readline())
for test_case in range(1,no_test_cases+1):
    grid = []
    grid_trans = []
    incomplete = False
    for tic_tac_row in range(4):
        grid.append(f.readline())
    for col in range(4):
        grid_trans.append('')
        for each in grid:
            grid_trans[col] += each[col]
            if each[col] == Blank:
                incomplete = True
    if not test_case == no_test_cases:
        f.readline() # Blank line
    winner = None
    # Row-wise check
    for row in grid:
        for cur_mark in (X,O):
            if row.count(cur_mark) == 4:
                winner = cur_mark
                break
            elif row.count(cur_mark) == 3 and row.find(T) > -1:
                winner = cur_mark
                break
    # Col-wise check
    if not winner:
        for col in range(4):
            for cur_mark in (X,O):
                if grid_trans[col].count(cur_mark) == 4:
                    winner = cur_mark
                    break
                elif grid_trans[col].count(cur_mark) == 3 and grid_trans[col].find(T) > -1:
                    winner = cur_mark
                    break
    # Diagonal Check
    if not winner:
        dia1 = grid[0][0]+grid[1][1]+grid[2][2]+grid[3][3]
        dia2 = grid[0][3]+grid[1][2]+grid[2][1]+grid[3][0]
        for cur_mark in (X,O):
            if dia1.count(cur_mark) == 4:
                winner = cur_mark
            elif dia1.count(cur_mark) == 3 and dia1.find(T) > -1:
                winner = cur_mark
            if dia2.count(cur_mark) == 4:
                winner = cur_mark
            elif dia2.count(cur_mark) == 3 and dia2.find(T) > -1:
                winner = cur_mark
    what_to_print = 'Case #'+str(test_case)+': '
    if winner:
        what_to_print += winner + ' won'
    elif incomplete:
        what_to_print += 'Game has not completed'
    else:
        what_to_print += 'Draw'
    what_to_print += chr(10)
    g.writelines(what_to_print)



