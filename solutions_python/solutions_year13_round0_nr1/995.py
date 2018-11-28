import sys

f = open(sys.argv[1])
T = int(f.readline())
for t in range(T):
    rows = [list(f.readline().strip()) for r in range(4)]
    columns = [[rows[i][j] for i in range(4)] for j in range(4)]
    diagonals = [[rows[i][i] for i in range(4)], [rows[i][3 - i] for i in range(4)]]

    answer = 'Draw'
    for player in ['X', 'O']:
        for line in rows + columns + diagonals:
            if line.count(player) + line.count('T') == 4:
                answer = '%s won' % player

            if answer == 'Draw' and '.' in line:
                answer = 'Game has not completed'

    print "Case #%d:" % (t + 1), answer
    f.readline()
