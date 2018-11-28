def smallest_row(place,r,c,board):
    for i in range(r):
        for j in range(c):
            if board[i,j] == place:
                return i
    return None # This should never happen
def smallest_col(place,r,c,board):
    for i in range(c):
        for j in range(r):
            if board[j,i] == place:
                return i
    return None # This should never happen

def largest_row(place,r,c,board):
    for i in range(r-1,-1,-1):
        for j in range(c-1,-1,-1):
            if board[i,j] == place:
                return i
    return None # This should never happen
def largest_col(place,r,c,board):
    for i in range(c-1,-1,-1):
        for j in range(r-1,-1,-1):
            if board[j,i] == place:
                return i
    return None # This should never happen

def valid_letter(letter,r,c,board):
    # Find the rectangle
    s = (smallest_row(letter,r,c,board), smallest_col(letter,r,c,board))
    l = (largest_row(letter,r,c,board), largest_col(letter,r,c,board))
    # Check all pieces
    for i in range(s[0],l[0]+1):
        for j in range(s[1], l[1]+1):
            if board[i,j] != letter:
                return False
    return True

for case in range(int(input())):
    r,c = map(int, input().split())
    board = {}
    for i in range(r):
        line = input()
        for j in range(c):
            board[i,j] = line[j]
    #
    letters = set(board.values())
    if "?" in letters:
        letters.remove("?")
    #
    possible_boards = []
    possible_boards.append(board)
    for i in range(r):
        for j in range(c):
            if board[i,j] == "?":
                new_boards = []
                for b in possible_boards:
                    for l in letters:
                        newb = dict(b)
                        newb[i,j] = l
                        new_boards.append(newb)
                possible_boards = new_boards
    #
    final = None
    for b in possible_boards:
        if all(valid_letter(l,r,c,b) for l in letters):
            final = b
            break
    # 
    print("Case #%d:"%(case+1))
    for i in range(r):
        print("".join(final[i,j] for j in range(c)))
