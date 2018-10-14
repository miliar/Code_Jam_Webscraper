import random

def one_click_test(board, empty, R, C):
    #print empty
    potential_c = []
    for cell in empty:
        if not is_empty(board, cell, empty, R, C):
            #print "cell", cell
            bombn = False
            adjempty = 0
            for n in get_neighbors(cell, R, C):
                #print "n", n
                if n not in empty:
                    bombn = True
                    #print "b"
                elif is_empty(board, n, empty, R, C):
                    adjempty += 1
                    #print "e"
            if bombn and adjempty == 0:
                #print "bad"
                return False, 1
        else:
            potential_c.append(cell)
    for c in potential_c:
        board_copy = [list(row) for row in board]
        if simulate_board(board_copy, c, empty, R, C):
            return True, c
    return False, 1

def one_click_test2(board, empty, R, C):
    #print empty
    for c in empty:
        board_copy = [list(row) for row in board]
        if simulate_board(board_copy, c, empty, R, C):
            return True, c
    return False, 1

def simulate_board(board, c, empty, R, C):
    #board_copy = [list(row) for row in board]
    #print print_board(board_copy, c)
    visited = set()
    def permeate(coor):
        r,co = coor
        board[r][co] = '*'
        visited.add(coor)
        if is_empty(board, coor, empty, R, C):
            for n in get_neighbors(coor, R, C):
                rn, cn = n
                if n in empty and n not in visited:
                    board[rn][cn] = '*'
                    visited.add(n)
                    if is_empty(board, n, empty, R, C):
                        permeate(n)
    permeate(c)
    #board_copy = [list(row) for row in board]
    #print print_board(board_copy, c)
    idealRow = ['*' for x in xrange(C)]
    for row in board:
        if row != idealRow:
            #print row
            #print idealRow
            return False
    return True
    

def is_empty(board, cell, empty, R, C):
    neighbors = get_neighbors(cell, R, C)
    for n in neighbors:
        if n not in empty:
            return False
    return True

def gen_random_continuous_board(R, C, M):
    empty = {}
    board = [['*' for col in xrange(C)] for row in xrange(R)]
    start = (random.choice(range(R)), random.choice(range(C)))
    #neighbors = get_neighbors(start)
    num_free = R*C - M
    while num_free > 0:
        neighbors = get_neighbors(start, R, C)
        sr, sc = start
        if board[sr][sc] == '*':
            board[sr][sc] = '.'
            empty[(sr,sc)] = 0
            num_free -= 1
        if num_free == 0:
            return board, empty
        #print (sr, sc), neighbors
        for k in xrange(len(neighbors)):
            r,c = neighbors[k]
            if board[r][c] == '*':
                board[r][c] = '.'
                empty[(r,c)] = 0
                num_free -= 1
            if num_free == 0:
                return board, empty
        start = random.choice(neighbors)
    return board, empty

def get_neighbors(coor, R, C):
    children = []
    r,c = coor
    for (dc, dr) in ((0,1),(-1,0),(1,0),(0,-1), (1,1),(-1,-1),(-1,1),(1,-1)):
        nc, nr = c + dc, r + dr
        if nc >=0 and nr >= 0 and nc <= C-1 and nr <= R-1:
                children.append((nr, nc))
    return children
        

def print_board(board, c):
    stringBoard = ''
    if c != None:
        ro, co = c
        board[ro][co] = 'c'
    for row in board:
        for col in row:
            stringBoard += col
        stringBoard += '\n'
    return stringBoard

def main(iterations):
    with open('outputsmallcorrected4.txt','w') as o:
        with open('C-small-attempt4.in', 'r') as f:
        #with open('sampleInput.txt', 'r') as f:
            T = int(f.readline())    
            for test_case in xrange(T):
                R, C, M = [int(x) for x in f.readline().split()]
                o.write("Case #" + str(test_case + 1) + ":\n")
                answer = "Impossible\n"
                for i in xrange(iterations):
                    board, empty = gen_random_continuous_board(R, C, M)
                    valid, c = one_click_test2(board, empty, R, C)
                    if valid:
                        answer = print_board(board, c)
                        #print answer
                        break
                    #else:
                        #print print_board(board, None)
                o.write(answer)
    

if __name__ == '__main__':
    main(2000)
