SAMPLE = open('sample_file.txt')
real_small = open('A-small-attempt0.in')
real_large = open('A-large.in')

def to_games_list(games_file):
    games = games_file
    T = int(games.readline())
    game = 0
    games_list = [[] for i in range(T)]
    for i in range(T):
        for n in range(4):
            games_list[game].append(games.readline()[:-1])
        games.readline()
        game += 1
    return games_list

def analyze_game(game):
    result_holder = check_horizontals(game)
    if result_holder[0]:
        return result_holder[1]
    result_holder = check_verticals(game)
    if result_holder[0]:
        return result_holder[1]
    result_holder = check_diagonals(game)
    if result_holder[0]:
        return result_holder[1]
    if draw_check(game):
        return 'Draw'
    return 'Game has not completed'

def check_horizontals(board):
    for row in board:
        num_xes = row.count('X')
        num_os = row.count('O')
        num_ts = row.count('T')
        if num_xes == 4 or (num_xes == 3 and num_ts == 1):
            return True,'X won'
        if num_os == 4 or (num_os == 3 and num_ts == 1):
            return True,'O won'
    return False,None

def check_verticals(board):
    to_rows = [[line[0] for line in board],
               [line[1] for line in board],
               [line[2] for line in board],
               [line[3] for line in board]]
    return check_horizontals(to_rows)

def check_diagonals(board):
    top_left = [board[i][i] for i in range(4)]
    top_right = [board[i][3-i] for i in range(4)]
    for diagonal in [top_left,top_right]:
        num_xes = diagonal.count('X')
        num_os = diagonal.count('O')
        num_ts = diagonal.count('T')
        if num_xes == 4 or (num_xes == 3 and num_ts == 1):
            return True,'X won'
        if num_os == 4 or (num_os == 3 and num_ts == 1):
            return True,'O won'
    return False,None

def draw_check(game):
    for row in game:
        if row.count('.') > 0:
            return False
    return True

def analyze_games(games_list):
    case = 1
    for game in games_list:
        print 'Case #' + str(case) + ': ' + analyze_game(game)
        case += 1

games_list = to_games_list(real_large)
analyze_games(games_list)
