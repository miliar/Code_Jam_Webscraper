import sys

basename  = sys.argv[0][0:-3]

#basename = basename + "-practice"
#basename = "A-small-attempt1" 
basename = "A-large"
#basename = basename + "-small"
#basename = basename + "-large"

input_filename = basename + ".in"
output_filename = basename + ".out"

input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

test_cases = int(input_file.readline().rstrip())

for case in range(1, test_cases+1):
    board = [list(input_file.readline().rstrip()) for i in range(4)]
    input_file.readline()

    tocheck = [row for row in board if row.count('.') == 0] # Rows

    cols = [[board[i][j] for i in range(4)] for j in range(4)]
    tocheck.extend([col for col in cols if col.count('.') == 0])

    diags = [[board[i][i] for i in range(4)], [board[i][3-i] for i in range(4)]]
    tocheck.extend([diag for diag in diags if diag.count('.') == 0])

    counts = [(line.count('X'),line.count('O'),line.count('T')) for line in tocheck]
    
    if counts.count((3,0,1)) > 0 or counts.count((4,0,0)) > 0:
        result = "X won"
    elif counts.count((0,3,1)) > 0 or counts.count((0,4,0)) > 0:
        result = "O won"
    else:
        if sum(line.count('.') for line in board) == 0:
            result = "Draw"
        else:
            result = "Game has not completed"

    output_file.write("Case #" + str(case) + ": " + result)
    if case < test_cases:
        output_file.write('\n')

