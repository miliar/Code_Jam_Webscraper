def checkLine(s):
    if s=='XXXX' or (s.count('X')==3 and s.count('T')==1):
        return 'X won'
    if s=='OOOO' or (s.count('O')==3 and s.count('T')==1):
        return 'O won'
    return ''
    

def solve(board):
    ## create 'check list' lines
    check = list(board)
    
    ## add columns
    for col in range(4):
        check.append(board[0][col]+board[1][col]+board[2][col]+board[3][col])

    ## add diagonals
    check.append(board[0][0]+board[1][1]+board[2][2]+board[3][3])
    check.append(board[0][3]+board[1][2]+board[2][1]+board[3][0])

    ## check for winner
    for item in check:
        r = checkLine(item)
        if r!='':
            return r

    ## check for not completed
    for line in board:
        if line.count('.')>0:
            return 'Game has not completed'

    return 'Draw'
                        
##            
## MAIN PROGRAMM
##
T = int(input())
for t in range(T):
    ## read case
    board = [input().rstrip() for _ in range(4)]
    input()
        
    ## solve and print results
    result = solve(board)
    print('Case #'+str(t+1)+': '+str(result))


    
