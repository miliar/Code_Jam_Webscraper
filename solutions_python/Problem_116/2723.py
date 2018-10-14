
def gameStatus(row):
    player_name = ''
    for x in row:
        if x == '.':
            return None

        if player_name != '' and player_name != x and x != 'T':
            return None

        if not x == 'T' and player_name == '':
            player_name = x
    return "%s won" % (player_name,)


def checkGame(case_num, game):
    game_copy = game[:]
    diagonals = [[],[]]
    for x in range(4):
        current_column = []
        for y in range(4):
            if x == y:
                diagonals[0].append(game[x][y])
            if y == (len(game[x]) - (x+1)):
                diagonals[1].append(game[x][y])
            current_column.append(game[y][x])
        game_copy.append(current_column)
    game_copy.extend(diagonals)

    game_completed = False
    game_status = ""
    for row in game_copy:
        if not row.count('.'):
            game_completed = True
        game_status = gameStatus(row)
        if not game_status:
            game_status = "Draw"
        else:
            break

    if not game_completed:
        print "Case #%d: Game has not completed" % (case_num,)
    else:
        print "Case #%d: %s" % (case_num, game_status)

def main():
    import sys
    number_of_games_left = int(sys.stdin.readline().strip())
    case_num = 1
    while case_num <= number_of_games_left:
        game = []
        for x in range(4):
            game_line = sys.stdin.readline()
            game.append(list(game_line.strip()))

        checkGame(case_num, game)
        if case_num < number_of_games_left:
            sys.stdin.readline()
        case_num += 1


if __name__ == "__main__":
    main()
