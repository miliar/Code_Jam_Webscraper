filename = "A-large"

def line_winner(line):
    xcount = line.count("X");
    ocount = line.count("O");
    tcount = line.count("T");

    if xcount + tcount == 4:
        return 'X'
    elif ocount + tcount == 4:
        return 'O'

def solve(rows):
    winner = None
    completed = True

    cols = [[], [], [], []]

    for i in range(len(rows)):
        row = rows[i]

        # Horizontal
        possible_winner = line_winner(row)
        if possible_winner:
            winner = possible_winner

        for j in range(len(row)):
            char = row[j]

            # Empty char
            if char == '.':
                completed = False

            cols[j].append(char)

    for i in range(len(cols)):
        col = cols[i]

        # Vertical
        possible_winner = line_winner(col)
        if possible_winner:
            winner = possible_winner

    # Diagonal
    diagonal = [rows[0][0], rows[1][1], rows[2][2], rows[3][3]]
    possible_winner = line_winner(diagonal)
    if possible_winner:
        winner = possible_winner

    diagonal = [rows[3][0], rows[2][1], rows[1][2], rows[0][3]]
    possible_winner = line_winner(diagonal)
    if possible_winner:
        winner = possible_winner

    status = "Game has not completed"
    if winner:
        status = winner + " won"
    elif completed:
        status = "Draw"

    return status

fi = open(filename + ".in", "r")
fo = open(filename + ".out", "w")

cases = int(fi.readline())

for case in range(cases):
    rows = []
    for i in range(4):
        line = fi.readline().replace("\n", "")
        row = list(line)
        rows.append(row)
    fi.readline()

    output = solve(rows)
    result = "Case #%d: %s\n" % (case + 1, output)
    print(result)
    fo.write(result)

fi.close()
fo.close()