def win(game, turn):
    replaced = [s.replace('T', turn) for s in game]

    for i in range(4):
        if replaced[i].count(turn) == 4:
            return True

    for j in range(4):
        s = ''
        for i in range(4):
            s += replaced[i][j]
        if s.count(turn) == 4:
            return 1

    s = ""
    for i in range(4):
        s += replaced[i][i]
    if s.count(turn) == 4:
        return 1

    s = ""
    for i in range(4):
        s += replaced[i][3 - i]
    if s.count(turn) == 4:
        return 1
    return 0


def draw(game):
    for i in range(4):
        for j in range(4):
            if game[i][j] == '.':
                return 0
    return 1


def main():
    inp = open('input.txt', 'r')
    out = open('output.txt', 'w')

    n = int(inp.readline())
    for i in range(0, n):
        game = [inp.readline() for j in range(4)]

        if win(game, 'O'):
            print('Case #{}: O won'.format(i+1), file=out)
        elif win(game, 'X'):
            print('Case #{}: X won'.format(i+1), file=out)
        elif draw(game):
            print('Case #{}: Draw'.format(i+1), file=out)
        else:
            print('Case #{}: Game has not completed'.format(i+1), file=out)

        inp.readline()

    inp.close()
    out.close()

if __name__ == '__main__':
    main()