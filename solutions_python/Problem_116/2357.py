import sys

def check_line(line):
    n_x = 0
    n_y = 0
    n_d = 0
    for c in line:
        if c == 'X':
            n_x += 1
        elif c == 'O':
            n_y += 1
        elif c == '.':
            n_d += 1
    if (n_x == 3 and n_y == 0 and n_d == 0) or n_x == 4:
        return n_d > 0, 'X'
    elif (n_y == 3 and n_x == 0 and n_d == 0) or n_y == 4:
        return n_d > 0, 'O'
    return n_d > 0, False

def outcome(game):
    draw = True
    lines = []
    for row in range(4):
        lines.append(game[row])
    for column in range(4):
        lines.append([game[row][column] for row in range(4)])
    lines.append([game[i][i] for i in range(4)])
    lines.append([game[3-i][i] for i in range(4)])

    for line in lines:
        end, winner = check_line(line)
        draw = draw and not end
        if winner != False:
            return winner +  " won"

    if draw:
        return "Draw"
    return "Game has not completed"

data = sys.stdin.readlines()

# Reading number of cases
n = int(data[0])

for r in range(n):
    # Reading 4 lines
    game = []
    for row in range(4):
        game.append([c for c in data[r*5 + row + 1][:-1]])

    # Checking
    print "Case #%d:"%(r+1), outcome(game)

