def check_board(board):
    full = True #Until we hear otherwise
    #Check across
    for i in range(4): #For each row
        row = board[i]
        result = check_sequence(row)
        if result == 1:
            return "X won"
        elif result == 2:
            return "O won"
        elif result == 3:
            full = False
    #Check down
    for i in range(4):
        col = []
        for j in range(4):
            col.append(board[j][i])
        #print("Checking sequence", col)
        result = check_sequence(col)
        if result == 1:
            return "X won"
        elif result == 2:
            return "O won"        
        elif result == 3:
            full = False
    #Check diagnonals
    seq = []
    for i in range(4):
        seq.append(board[i][i])
    result = check_sequence(seq)
    if result == 1:
        return "X won"
    elif result == 2:
        return "O won"        
    elif result == 3:
        full = False    
    
    seq = []
    for i in range(4):
        seq.append(board[i][3 - i])
    result = check_sequence(seq)
    if result == 1:
        return "X won"
    elif result == 2:
        return "O won"        
    elif result == 3:
        full = False         
    
    #Nobody won... which is it?
    if full:
        return "Draw"
    else:
        return "Game has not completed"
    
#Checks whether the 4 charaters in seq are...
#1 - win for x
#2 - win for y
#3 - incomplete row
#4 - complete row
def check_sequence(seq):
    could_be_x = True
    could_be_o = True
    for sym in seq:
        if sym == ".":
            return 3
        if sym == "O":
            could_be_x = False
        if sym == "X":
            could_be_o = False
    if could_be_x:
        return 1
    elif could_be_o:
        return 2
    else:
        return 4

file = open("qual_large.txt")
T = int(file.readline())
cur_case = 1
while cur_case <= T:
    case = []
    for i in range (4): #Pick out the 4 rows
        string = file.readline().rstrip()
        row = list(string)
        case.append(row)
    result = check_board(case)
    print("Case #" + str(cur_case) + ": " + str(result))
    cur_case += 1
    file.readline() #throw away blank
