import sys

def rows(game):
    return (set(i) for i in game)

def columns(game):
    for i in range(4):
        yield {game[0][i],
               game[1][i],
               game[2][i],
               game[3][i]
        }

def diagonals(game):
    return (
        {game[0][0], game[1][1], game[2][2], game[3][3]},
        {game[3][0], game[2][1], game[1][2], game[0][3]},
    )

def check_winner(row):
    if 'X' in row:
        return 2
    elif 'O' in row:
        return 3
    else:
        raise Exception("Unexpected state {}".format(row))

def check(game):
    finished = 1
    for row in game:

        if '.' in row:
            finished = 0
        elif len(row) == 1:
            return check_winner(row)
        elif len(row) == 2:
            if 'T' in row:
                return check_winner(row)

    return finished

def get_state(game):

    state = check(rows(game))
    if state > 1:
        return state

    state = check(columns(game))
    if state > 1:
        return state

    state = check(diagonals(game))

    return state

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: %s input_file".format(sys.argv[0]))

    input_file = sys.argv[1]
    with open(input_file) as input:
        T = int(input.readline().strip())

        for i in range(T):
            game = [
                input.readline().strip(),
                input.readline().strip(),
                input.readline().strip(),
                input.readline().strip(),
            ]

            input.readline()

            state = get_state(game)

            outcome = ""
            if state == 0:
                outcome = "Game has not completed"
            elif state == 1:
                outcome = "Draw"
            elif state == 2:
                outcome = "X won"
            else:
                outcome = "O won"

            print("Case #{}: {}".format(i+1, outcome))