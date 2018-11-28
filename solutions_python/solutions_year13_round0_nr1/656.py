# the main function that outputs to a file
def a(filename):
    fd = open(filename, 'rU')
    cases = int(fd.readline())
    out = []
    #read the file here
    temp = fd.readlines()
    fd.close()
    for i in range(cases):
        l1 = temp[i*5].rstrip()
        l2 = temp[i*5+1].rstrip()
        l3 = temp[i*5+2].rstrip()
        l4 = temp[i*5+3].rstrip()
        result = game_state((l1, l2, l3, l4))
        out.append('Case #{0}: {1}'.format(i+1, result))

    #write to the output file
    fd = open('output.txt', 'w')
    for s in out:
        fd.write(s+'\n')
    fd.close()

# the subfunction that does most of the computation
def game_state(board):
    """Determines game state

    game_state((str,str,str,str)) -> str

    """
    
    d1 = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    d2 = board[0][3] + board[1][2] + board[2][1] + board[3][0]
    h1 = board[0]
    h2 = board[1]
    h3 = board[2]
    h4 = board[3]
    v1 = col_string(board, 0)
    v2 = col_string(board, 1)
    v3 = col_string(board, 2)
    v4 = col_string(board, 3)
    lines = [d1, d2, h1, h2, h3, h4, v1, v2, v3, v4]
    for s in lines:
        if alpha_sort(s) in ['TXXX','XXXX']:
            return 'X won'
        elif alpha_sort(s) in ['OOOT','OOOO']:
            return 'O won'
    if any('.' in s for s in lines):
        return 'Game has not completed'
    else:
        return 'Draw'
    
def alpha_sort(string):
    temp = []
    for c in string:
        temp.append(c)
    temp.sort()
    return ''.join(temp)

def col_string(board, col):
    return board[0][col]+board[1][col]+board[2][col]+board[3][col]
