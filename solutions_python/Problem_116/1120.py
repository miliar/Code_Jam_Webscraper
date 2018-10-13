f = open('A-large.in')

num_test_cases = int(f.readline())

counts = {}

def reset_counts():
    global counts
    counts = {"X": {"rows":[0,0,0,0], "cols":[0,0,0,0], "diags":[0,0]},
        "O": {"rows":[0,0,0,0], "cols":[0,0,0,0], "diags":[0,0]}}

def inc_counts(row, col, player):
    global counts
    counts[player]["rows"][row] += 1
    counts[player]["cols"][col] += 1
    if row == col:
        counts[player]["diags"][0] += 1
    if row == 3 - col:
        counts[player]["diags"][1] += 1

def player_wins(player):
    global counts
    for count in counts[player]["rows"]:
        if count == 4:
            return True
    for count in counts[player]["cols"]:
        if count == 4:
            return True
    for count in counts[player]["diags"]:
        if count == 4:
            return True
    return False
        

for test_case in range(num_test_cases):
    # Read in test case
    board = []
    for i in range(4):
        board.append(f.readline().strip())

    # Count up lines
    reset_counts()
    empty_cells = False
    for row in range(4):
        for col in range(4):
            token = board[row][col]
            if token == ".":
                empty_cells = True
            elif token == "T":
                inc_counts(row, col, "X")
                inc_counts(row, col, "O")
            else:
                inc_counts(row, col, token)

    x_wins = player_wins("X")
    o_wins = player_wins("O")
    
    # Output
    print "Case #"+str(test_case+1)+":",
    if x_wins and o_wins:
        print "Draw"
    elif x_wins:
        print "X won"
    elif o_wins:
        print "O won"
    elif empty_cells:
        print "Game has not completed"
    else:
        print "Draw"

    f.readline()
                

f.close()
