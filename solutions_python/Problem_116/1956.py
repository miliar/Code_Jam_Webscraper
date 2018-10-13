with open('A-large.in') as input_data:
    n = int(input_data.readline())
    games = []
    for i in range(n):
        games.append([])
        for y in range(4):
            games[i].append(input_data.readline().rstrip())
        input_data.readline()
print(games)
empty_fields = 0

def check_game(game):
    def check_row(row):
        global empty_fields
        res = {'T': 0, 'X': 0, 'O': 0, '.': 0}
        for i in row:
            res[i] += 1
        empty_fields += res['.']
        if (res['X'] == 3 and res['T'] == 1) or res['X'] == 4:
            return 'X'
        if (res['O'] == 3 and res['T'] == 1) or res['O'] == 4:
            return 'O'
        return None

    def check_column(column_i):
        column = [row[column_i] for row in game]
        return check_row(column)

    def check_diagonals():
        diagonal1 = [row[i] for i, row in enumerate(game)]
        diagonal2 = [row[3-i] for i, row in enumerate(game)]
        return check_row(diagonal1) or check_row(diagonal2)

    for i, line in enumerate(game):
        res = check_row(line)
        if res:
            return res
        res2 = check_column(i)
        if res2:
            return res2
    res3 = check_diagonals()
    if res3:
        return res3
    if empty_fields > 0:
        print(empty_fields)
        return 'not'
    else:
        print(empty_fields)
        return 'draw'


with open('A-small-practice.out', 'w') as output_data:
    for i, game in enumerate(games):
        res = check_game(game)
        empty_fields = 0
        if res == 'X' or res == 'O':
            output_data.write("Case #%d: %s won\n" % (i+1, res))
        if res == 'not':
            output_data.write("Case #%d: Game has not completed\n" % (i+1))
        if res == 'draw':
            output_data.write("Case #%d: Draw\n" % (i+1))

