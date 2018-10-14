import string
#daniel hammack
def processfile(path):
    fout = open(string.replace(path,'in','out'), 'w')
    with open(path,'r') as f:
        lines = f.readlines()

    lines = [string.replace(l,'\n', '') for l in lines]
    lines = [l for l in lines if len(l) > 0]
    cases = int(lines[0])
    for i in range(0,cases):
        board = []
        board.extend(lines[1 + (i*4):5+(i*4)])
        fout.write('Case #' + str(i+1) + ': ' + processboard(board) + '\n')
            
    fout.close()

#determine a winner.
def processboard(board):
    #diagonals
    #print board
    ldiag,rdiag = ([board[i][i] for i in xrange(0,4)],
                   [board[3-i][i] for i in xrange(0,4)])

    if result(ldiag) != 'nowinner':
        return result(ldiag)
    elif result(rdiag) != 'nowinner':
        return result(rdiag)

    for i in range(0,4):
        vert = [board[j][i] for j in range(0,4)]
        horiz = [board[i][j] for j in range(0,4)]
        
        if result(vert) != 'nowinner':
            return result(vert)
        elif result(horiz) != 'nowinner':
            return result(horiz)

    final = draw_or_incomplete(board)
    if final == 'i':
        return 'Game has not completed'
    elif final == 'd':
        return 'Draw'
    
#returns d for draw, i for incomplete
def draw_or_incomplete(board):
    for i in board:
        for j in i:
            if j == '.':
                return 'i'
    return 'd'
    
#returns the winner a group
def result(group):
    for item in ['X','O']:
        if group.count(item) == 4:
            return item + ' won'
        elif group.count(item) == 3 and group.count('T') == 1:
            return item + ' won'
    return 'nowinner'


processfile('C:\\users\\daniel\\desktop\\a-large.in')
