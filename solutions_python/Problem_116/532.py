import sys

def hasWon(game0, player):
    game = []
    for line in game0:
        game.append(line.replace('T', player))
    four = player*4
    return (player*4 in game) or \
           ((player,)*4 in zip(*game)) or \
           all(map(lambda c: c is player, [game[i][i] for i in range(4)])) or \
           all(map(lambda c: c is player, [game[i][3-i] for i in range(4)]))

def gameStatus(game):
    if hasWon(game, 'X'):
        return 'X won'
    if hasWon(game, 'O'):
        return 'O won'
    if any(map(lambda line: '.' in line, game)):
        return 'Game has not completed'
    return 'Draw'

s = sys.stdin
T = int(s.readline())
for t in range(T):
    sys.stdout.write("Case #{}: {}\n".format(t + 1,
        gameStatus([s.readline().strip() for _ in range(4)])))
    s.readline()
