nb = int(input())

def winner(game):
    for i in range(4):
        if any((
                all(game[i][j] in ('X', 'T') for j in range(4)),
                all(game[j][i] in ('X', 'T') for j in range(4)),
                all(game[3-j][j] in ('X', 'T') for j in range(4)),
                )):
            return 'X won'

        if any((
                all(game[i][j] in ('O', 'T') for j in range(4)),
                all(game[j][i] in ('O', 'T') for j in range(4)),
                all(game[j][j] in ('O', 'T') for j in range(4)),
                all(game[3-j][j] in ('O', 'T') for j in range(4)),
                )):
            return 'O won'

    if any('.' in g for g in game):
        return 'Game has not completed'
    return 'Draw'


for i in range(nb):
    game = []
    for j in range(4):
        game.append(list(input()))
    print("Case #%s: %s" % (i + 1, winner(game)))
    input()
