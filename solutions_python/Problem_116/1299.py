def check_win(game, turn):
    replaced = [s.replace('T', turn) for s in game]
    #hot
    for i in range(4):
        if replaced[i].count(turn) == 4:
            return True
    #ver
    for j in range(4):
        s = ''
        for i in range(4):
            s += replaced[i][j]
        if s.count(turn) == 4:
            return True
    #diag
    s = ''
    for i in range(4):
        s += replaced[i][i]
    if s.count(turn) == 4:
        return True
    #diag
    s = ''
    for i in range(4):
        s += replaced[i][3 - i]
    if s.count(turn) == 4:
        return True
    return False


def check_draw(game):
    for i in range(4):
        if game[i].count('.') != 0:
            return False
    return True


def main():
    n = int(input())
    for i in range(1, n + 1):
        game = [input() for j in range(4)]

        if check_win(game, 'O'):
            print('Case #{}: O won'.format(i))
        elif check_win(game, 'X'):
            print('Case #{}: X won'.format(i) )
        elif check_draw(game):
            print('Case #{}: Draw'.format(i) )
        else:
            print('Case #{}: Game has not completed'.format(i) )
        input()

if __name__ == '__main__':
    main()