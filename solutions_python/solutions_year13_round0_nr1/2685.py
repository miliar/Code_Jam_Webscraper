def parse(line):
    #print ("Parsing line: "+line)
    return [line[0],line[1],line[2],line[3]]
def isPlayer(c):
    return c == 'X' or c == 'O'
def check(b): # we check three sets, rows, cols, and diags
    isFull = True
    winner=''
    for x in range(0,4):# this loop checks rows
        cur = b[x][0] # this is our line status where a line is a row/col/diag
        broken = False # indicates whether we left the loop normally; if normally, then we have a winner
        for y in range(1,4): # go from 1 to 3 since we already looked at the beginning of the line
            c = b[x][y] # current tile
            if cur == 'T' and isPlayer(c): # if the first tile was a T, then we want it to convert to the first player we come across
                cur = c
            elif c == '.': # an empty spot means that this line can't possibly be a winner and that the game can't be a draw
                isFull = False
                broken = True
                break
            elif c == 'T': # don't do anything since this is the wildcard
                continue
            elif c != cur: # conflict! means that this line is not a winner
                broken = True
                break
        if not broken: # if we exited the loop normally, then we have a winner!
            winner = cur
            break
    if winner != '': # we always want to check between sets
        print ("Case #"+str(tc)+": "+winner+ " won")
        return
    for x in range(0,4): # checks cols
        cur = b[0][x]
        broken = False
        for y in range(1,4):
            c = b[y][x]
            if cur == 'T' and isPlayer(c):
                cur = c
            elif c == '.':
                isFull = False
                broken = True
                break
            elif c == 'T':
                continue
            elif c != cur:
                broken = True
                break
        if not broken:
            winner = cur
            break

    if winner != '':
        print ("Case #"+str(tc)+": "+winner+ " won")
        return

    cur = b[0][0]
    broken = False
    for y in range(1,4): # checks one diag
        c = b[y][y]
        if cur == 'T' and isPlayer(c):
            cur = c
        elif c == '.':
            isFull = False
            broken = True
            break
        elif c == 'T':
            continue
        elif c != cur:
            broken = True
            break
    if not broken:
        winner = cur
    
    if winner != '':
        print ("Case #"+str(tc)+": "+winner+ " won")
        return
    
    cur = b[0][3]
    broken = False
    for y in range(1,4): # checks other diag
        c = b[y][3 - y]
        if cur == 'T' and isPlayer(c):
            cur = c
        elif c == '.':
            isFull = False
            broken = True
            break
        elif c == 'T':
            continue
        elif c != cur:
            broken = True
            break
    if not broken:
        winner = cur
    
    if winner != '':
        print ("Case #"+str(tc)+": "+winner+ " won")
        return
    else:
        if isFull:
            print ("Case #"+str(tc)+": Draw")
        else:
            print ("Case #"+str(tc)+": Game has not completed")
    



tcs=int(input())

# each loop is a different testcase
for tc in range(1,tcs+1):
    board=[]
    # read in the board a line at a time into a 4x4 array
    for i in range(0,4):
        board.append(parse(input()))
    # this checks the board 
    check(board)
    #print (board)
    input()
    #for i in range(0,3):
        #print (file.readline()[:-1])

