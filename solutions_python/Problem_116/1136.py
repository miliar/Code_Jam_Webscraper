import sys
import fileinput


def getCols(rows):
    cols = ['', '', '', '']

    for row in rows:
        cols[0] += row[0]
        cols[1] += row[1]
        cols[2] += row[2]
        cols[3] += row[3]

    return cols


def getDiags(rows):
    diags = []

    diags.append(rows[0][0] + rows[1][1] + rows[2][2] + rows[3][3])
    diags.append(rows[3][0] + rows[2][1] + rows[1][2] + rows[0][3])

    return diags


def getGames(filename):

    with fileinput.input(files=filename) as f:
        # Don't need the first line (number of games)
        f.readline()
        games = {}

        line = f.readline()
        while line:
            game = int((f.lineno() - 1) / 5)

            rows = []
            rows.append(line.strip())
            rows.append(f.readline().strip())
            rows.append(f.readline().strip())
            rows.append(f.readline().strip())
            games[game] = rows + getCols(rows)
            games[game] = games[game] + getDiags(rows)

            f.readline()
            line = f.readline()

        return games


def testGame(game):
    maybe_i = False

    for case in game:
        if case.find('.') > -1:
            maybe_i = True
            continue

        side = None
        if 'X' in case:
            side = 'X'
        elif 'O' in case:
            side = 'O'
        else:
            continue

        if case.replace('T', side).count(side) == 4:
            return "{} won".format(side)

    if maybe_i:
        return "Game has not completed"

    return "Draw"


def testGames(games):
    result = ''
    for num, game in games.items():
        result += "Case #{}: {}\n".format(num + 1, testGame(game))

    return result


if __name__ == "__main__":
    filename = sys.argv[1]
    games = getGames(filename)
    output_file = open(filename.replace('in', 'out'), 'w')
    output_file.write(testGames(games))
    output_file.close()
