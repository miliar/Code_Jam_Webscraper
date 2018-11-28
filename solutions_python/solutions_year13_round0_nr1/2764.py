# Evaluates games of tictactoe

GAME_INCOMPLETE = 0
O_WINS = 1
X_WINS = 2
DRAW = 3
UNKNOWN = 4

def read_file(filename):
    input = open(filename, 'r')
    lines = input.readlines()
    num_games = int(lines[0])
    output = [UNKNOWN] * num_games
    
    # Evaluate each game
    for game_id in range(num_games):
        #print 'Resolving game ' , game_id
        # Each game has 5 lines
        game_index = game_id * 5 + 1
        #print 'Game index' , game_index
        game = lines[game_index].strip() + lines[game_index + 1].strip() + lines[game_index + 2].strip() + lines[game_index + 3].strip()
        #print 'Game as line ', game
        
        # initialise variables
        resolved = False
        game_incomplete = False
        case = 0
        
        # Evaluate cases until resolved, i.e. someone has won, or all cases have been evaluated
        while(resolved == False and case < 10):
            row = get_case(case, game)
            #print 'game ' , game_id , ': case ' , case , ' row: ' , row
            game_incomplete, resolved = evaluate(game_id, row, output)
            case = case + 1
        
        # Now all rows have been evaluated or the game has been won, output the result
        if (resolved):
            output_status(game_id, output[game_id])
        elif (game_incomplete):
            output_status(game_id, GAME_INCOMPLETE)
        else:
            output_status(game_id, DRAW)

def get_case(case_id, rows):
    # Horizontal
    if case_id == 0:
        return rows[0] , rows[1], rows[2], rows[3]
    if case_id == 1:
        return rows[4] , rows[5], rows[6], rows[7]
    if case_id == 2:
        return rows[8] , rows[9], rows[10], rows[11]
    if case_id == 3:
        return rows[12] , rows[13], rows[14], rows[15]
    # vertical
    if case_id == 4:
        return rows[0] , rows[4], rows[8], rows[12]
    if case_id == 5:
        return rows[1] , rows[5], rows[9], rows[13]
    if case_id == 6:
        return rows[2] , rows[6], rows[10], rows[14]
    if case_id == 7:
        return rows[3] , rows[7], rows[11], rows[15]
    # Diagonal
    if case_id == 8:
        return rows[0] , rows[5], rows[10], rows[15]
    if case_id == 9:
        return rows[3] , rows[6], rows[9], rows[12]

# Returns the status of a single Tic-Tac-Toe line: True if there was a win or false otherwise. Also marks game incomplete if a space is discovered.
def evaluate(game_id, case, output):
    first = case[0]
    if (first == 'T'):
        first = case[1]
    game_incomplete = False
    same = 0

    # Loop over all input so we can discover any incomplete spaces.
    for i in range(len(case)):
        current = case[i]
        if current == '.':
            game_incomplete = True
        elif (current == first or current == 'T'):
            same = same + 1
    
    # Return false if all unknown or there is a draw
    if (same < 4):
        return game_incomplete, False
    elif (first == 'O'):
        output[game_id] = O_WINS
    elif (first == 'X'):
        output[game_id] = X_WINS
    # Return true if there is a win
    return game_incomplete, True

def output_status(game_id, status):
    if (status == GAME_INCOMPLETE):
        print 'Case #{0}: Game has not completed'.format(game_id + 1)
    elif (status == O_WINS):
        print 'Case #{0}: O won'.format(game_id + 1)
    elif (status == X_WINS):
        print 'Case #{0}: X won'.format(game_id + 1)
    elif (status == DRAW):
        print 'Case #{0}: Draw'.format(game_id + 1)
    elif (status == UNKNOWN):
        print 'Case #{0}: UNKNOWN'.format(game_id + 1)

#read_file('tictactoe_sample_input.txt')
read_file('A-small-attempt1.in')