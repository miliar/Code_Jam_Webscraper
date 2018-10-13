boards = open('attempt1.txt', 'r')
input_text = boards.read()

cases = ''
for i in input_text:
    if i == "\n":
        break
    cases = cases + i
cases = int(cases)


def parse(text, times): # converts input text into lists of boards
    i = 0
    list_boards = []
    for _ in range(times):
        list_boards.append([])
    for j in text:
        if j == '.' or j == 'T' or j == 'O' or j == 'X':
            list_boards[i].append(j)
            if len(list_boards[i]) == 16:
                i += 1
    return list_boards

games = parse(input_text, cases)

winners = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],[0,5,10,15],[3,6,9,12]]

def evaluator(boards):
    results = []
    i = 0
    for board in boards:
        result = check_win(board)
        if result == 'X' or result == 'O':
            results.append(check_win(board))
        elif result == False:
            if '.' in board:
                results.append('unfinished')   
            else:
                results.append('draw')
    for result in results:
        i += 1
        if result == 'X' or result == 'O':
            print('Case #' + str(i) + ': ' + result + ' won')
        elif result == 'unfinished':
            print('Case #' + str(i) + ': Game has not completed')
        elif result == 'draw':
            print('Case #' + str(i) + ': Draw')


def check_win(board): # returns winner or False
    for line in winners:
        x, o = 0, 0
        for spot in line:
            if board[spot] == 'X':
                x += 1
            elif board[spot] == 'O':
                o += 1
            elif board[spot] == 'T':
                x += 1
                o += 1
        if x == 4:
            return 'X'
        if o == 4:
            return 'O'
    return False 


evaluator(games)

