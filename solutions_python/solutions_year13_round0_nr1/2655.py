'''
Created on 14/04/2013

@author: Adam
'''

winners = []

def addwinner(winner):
    winners.append(winner + ' won')


def processboard(board):
    # Check horizontal rows
    for r in range(0,4):
        prev = board[r][0]
        i = 1
        while i < 4:
            nextchar = board[r][i]
            if nextchar == '.':
                i = 5
            elif prev == 'T' or nextchar == 'T' or prev == nextchar:
                prev = nextchar
                i += 1
            else:
                i = 5
            if i == 4:
                if prev == 'T':
                    prev = board[r][0]
                addwinner(prev)
                return

    # Check vertical columns            
    for c in range(0,4):
        prev = board[0][c]
        i = 1
        while i < 4:
            nextchar = board[i][c] 
            if nextchar == '.':
                i = 5   
            if prev == 'T' or nextchar == 'T' or prev == nextchar:
                prev = nextchar
                i += 1
            else:
                i = 5
            if i == 4:
                if prev == 'T':
                    prev = board[0][c]
                addwinner(prev)
                return
            
    # Check diagonals
    prev = board[0][0]
    i = 1
    while i < 4:
        nextchar = board[i][i]    
        if nextchar == '.':
            i = 5
        if prev == 'T' or nextchar == 'T' or prev == nextchar:
            prev = nextchar
            i += 1
        else:
            i = 5
        if i == 4:
            if prev == 'T':
                prev = board[0][0]
            addwinner(prev)
            return
        
    prev = board[0][3]
    r = 1
    c = 2
    while r < 4:
        nextchar = board[r][c]    
        if nextchar == '.':
            r = 5
        if prev == 'T' or nextchar == 'T' or prev == nextchar:
            prev = nextchar
            r += 1
            c -= 1
        else:
            r = 5
        if r == 4:
            if prev == 'T':
                prev = board[0][3]
            addwinner(prev)
            return
        
    # No winner! Is game over?
    if '.' in board[0] or '.' in board[1] or '.' in board[2] or '.' in board[3]:
        winners.append('Game has not completed')
    else:
        winners.append('Draw')
            
infile = open('qa_input_1_easy.txt', 'r')
cases = infile.readline()
print cases

count = 0
board = []
for line in infile.readlines():
    print line, count
    if count < 4:
        board.append(line.strip())
        count += 1
    else:
        count = 0
        processboard(board)
        board = []
        
outfile = open('output.txt', 'w')
count = 0
for winner in winners:
    count += 1 
    outfile.write('Case #' + str(count) + ': ' + winner + '\n')

infile.close()    
outfile.close()

