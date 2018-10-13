__author__ = 'Mariyan Stoyanov'

def charsAtPosition(position, grid):
    s = set()
    for p in position:
        i,j = p
        s.add(grid[i][j])
    return s

def winningAtPositions(positions, grid, winning_chars):
    for p in positions:
        s = charsAtPosition(p, grid)
        if s<=winning_chars:
            return True
    return False

of = open('output.txt', 'w')

f = open('A-large.in', 'r')

counter = 0

number_of_test_cases = 0
row = 0

test_cases = []
games_list = []
game = []

playerX = set(['T','X'])
playerO = set(['T','O'])

winning_positions = []

NUMBER_OF_ROWS = 4
NUMBER_OF_COLS = NUMBER_OF_ROWS

LT_RB_diag_win = []
row_wins = []

for i in range(NUMBER_OF_ROWS):
    row_i_win = []

    for j in range(NUMBER_OF_COLS):
        row_i_win.append(tuple([i,j]))
        if i==j:
            LT_RB_diag_win.append(tuple([i,j]))

    row_wins.append(row_i_win)

RT_LB_diag_win = []
col_wins = []

for j in range(NUMBER_OF_COLS):
    col_j_win = []
    jreverse = NUMBER_OF_COLS-j-1
    for i in range(NUMBER_OF_ROWS):
        col_j_win.append(tuple([i,jreverse]))
        if i+jreverse==(NUMBER_OF_COLS-1):
            RT_LB_diag_win.append(tuple([i,jreverse]))

    col_wins.append(col_j_win)


winning_positions.append(LT_RB_diag_win)
winning_positions.append(RT_LB_diag_win)
winning_positions.extend(row_wins)
winning_positions.extend(col_wins)


for line in f:
    if len(line.rstrip(' \t\n'))==0:
        row = 0
        if len(game)==NUMBER_OF_ROWS:
            games_list.append(tuple(game))
        game = []
    else:
        if counter==0:
            number_of_test_cases = int(line)
            row = 0
        else:
            game.append(list(line.rstrip('\n')))
            row += 1
        counter += 1

if row!=0:
    games_list.append(game)

print len(games_list)
if(len(games_list)!=number_of_test_cases):
    raise ValueError('number of test cases read from file does not match the indicated number of test cases that should be there')

f.close()

for case_num in range(len(games_list)):
    grid = games_list[case_num]

    if winningAtPositions(winning_positions, grid, playerX):
        print 'Case #%d: X won'%(case_num+1)
        of.write('Case #%d: X won'%(case_num+1))
    elif winningAtPositions(winning_positions, grid, playerO):
        print 'Case #%d: O won'%(case_num+1)
        of.write('Case #%d: O won'%(case_num+1))
    else:
        gameNotComplete = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='.':
                    gameNotComplete=True
                    break
        if gameNotComplete==False:
            print 'Case #%d: Draw'%(case_num+1)
            of.write('Case #%d: Draw'%(case_num+1))
        else:
            print 'Case #%d: Game has not completed'%(case_num+1)
            of.write('Case #%d: Game has not completed'%(case_num+1))

    of.write('\n')
of.close()

 

 