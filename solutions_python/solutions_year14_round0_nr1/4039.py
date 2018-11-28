
file = open('input', 'r')
lines = file.read().splitlines()

num_games = int(lines.pop(0))

for i in range(num_games):
    game = lines[i * 10:(i + 1) * 10]

    first_guess = int(game[0])
    first_board = game[1:5]
    second_guess = int(game[5])
    second_board = game[6:10]

    first_row = first_board[first_guess - 1].split(" ")
    second_row = second_board[second_guess - 1].split(" ")
    possibilities = set(first_row) & set(second_row)

    if len(possibilities) == 1:
        print("Case #{:d}: {:s}".format(i + 1, tuple(possibilities)[0]))
    elif len(possibilities) > 1:
        print("Case #{:d}: Bad magician!".format(i + 1))
    else:
        print("Case #{:d}: Volunteer cheated!".format(i + 1))