#### Problem A. Tic-Tac-Toe-Tomek ####

# input
filename = "A-large.in"
lines = (line.rstrip('\n') for line in open(filename))
T = int(lines.__next__())

# output
output = open('output', 'w+')

for caseIdx in range(T):

    # parse grid
    grid = []
    for _ in range(4):
        grid.append(list(lines.__next__()))

    # logic
    rows = [[(i, j) for j in range(4)] for i in range(4)]
    cols = [[(i, j) for i in range(4)] for j in range(4)]
    diags = [[(i, i) for i in range(4)], [(i, 3-i) for i in range(4)]]

    msg = ''

    for line in rows + cols + diags:
        # read line
        syms = []
        for (i, j) in line:
            syms += grid[i][j]

        if all(map(lambda x: x == "X" or x == 'T', syms)):
            msg = "X won"
            break
        elif all(map(lambda x: x == "O" or x == 'T', syms)):
            msg = "O won"
            break

    if msg == '':
        if all(map(lambda row: all(map(lambda x: x != '.', row)), grid)):
            msg = 'Draw'
        else:
            msg = 'Game has not completed'

    output.write('Case #' + str(caseIdx + 1) + ': ' + msg + '\n')

    # Each test case is followed by an empty line
    try:
        lines.__next__()
    except StopIteration:
        pass

output.close()
print(open('output', 'r').read())
