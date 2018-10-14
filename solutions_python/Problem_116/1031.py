def doChecks(s):
    X = s.count('X')
    O = s.count('O')
    T = s.count('T')
    empties = row.count('.')
    out_str = ""
    if X+T == 4:
        out_str = "X won"
    if O+T == 4:
        out_str = "O won"
    return out_str, empties

fInput = open("qr_A-large.in", 'r')
fOutput = open("qr_A-large.out", 'w')

num_cases = int(fInput.next())

for case in range(1,num_cases+1):
    print '.',
    board = []
    for i in range(4):
        board.append(fInput.next()[:4])
        
    out_str = ""
    fullRows = 0 # is 4 if the board is full
    
    # check rows
    for row in board:
        out_str, empties = doChecks(row)
        if len(out_str)> 0: break
        if empties == 0: fullRows += 1 
            
    if len(out_str)==0: # if not finished yet
        #check columns
        for colID in range(4):
            col = ''.join([x[colID] for x in board])
            out_str, empties = doChecks(col)
            if len(out_str)> 0: break
    
    if len(out_str)==0: # if not finished yet
        # check diag1
        diag1 = ''.join(board[i][i] for i in range(4))
        out_str, empties = doChecks(diag1)
        
    if len(out_str)==0: # if not finished yet
        # check diag2
        diag2 = ''.join(board[i][3-i] for i in range(4))
        out_str, empties = doChecks(diag2)
        
    if len(out_str) == 0:
        if fullRows == 4:
            out_str = "Draw"
        else:
            out_str = "Game has not completed"
    fOutput.write("Case #{0}: ".format(case) + out_str + "\n")
    if case < num_cases: fInput.next()
    
fInput.close()
fOutput.close()
print "\t[DONE]"