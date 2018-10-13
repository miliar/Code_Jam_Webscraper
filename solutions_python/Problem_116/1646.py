input = open("A-small-attempt2.in", "r")
output = open("A-small-attempt2.out", "w")

numCases = int(input.readline())
for caseNum in range(numCases):
    board = [input.readline().strip(), input.readline().strip(), input.readline().strip(), input.readline().strip()]
    input.readline()
    
    XWon =  ((board[0][0] == "T" or board[0][0] == "X") and
       (board[0][1] == "T" or board[0][1] == "X") and
       (board[0][2] == "T" or board[0][2] == "X") and
       (board[0][3] == "T" or board[0][3] == "X")) or \
       ((board[1][0] == "T" or board[1][0] == "X") and
       (board[1][1] == "T" or board[1][1] == "X") and
       (board[1][2] == "T" or board[1][2] == "X") and
       (board[1][3] == "T" or board[1][3] == "X")) or \
       ((board[2][0] == "T" or board[2][0] == "X") and
       (board[2][1] == "T" or board[2][1] == "X") and
       (board[2][2] == "T" or board[2][2] == "X") and
       (board[2][3] == "T" or board[2][3] == "X")) or \
       ((board[3][0] == "T" or board[3][0] == "X") and
       (board[3][1] == "T" or board[3][1] == "X") and
       (board[3][2] == "T" or board[3][2] == "X") and
       (board[3][3] == "T" or board[3][3] == "X")) or \
       ((board[0][0] == "T" or board[0][0] == "X") and
       (board[1][0] == "T" or board[1][0] == "X") and
       (board[2][0] == "T" or board[2][0] == "X") and
       (board[3][0] == "T" or board[3][0] == "X")) or \
       ((board[0][1] == "T" or board[0][1] == "X") and
       (board[1][1] == "T" or board[1][1] == "X") and
       (board[2][1] == "T" or board[2][1] == "X") and
       (board[3][1] == "T" or board[3][1] == "X")) or \
       ((board[0][2] == "T" or board[0][2] == "X") and
       (board[1][2] == "T" or board[1][2] == "X") and
       (board[2][2] == "T" or board[2][2] == "X") and
       (board[3][2] == "T" or board[3][2] == "X")) or \
       ((board[0][3] == "T" or board[0][3] == "X") and
       (board[1][3] == "T" or board[1][3] == "X") and
       (board[2][3] == "T" or board[2][3] == "X") and
       (board[3][3] == "T" or board[3][3] == "X")) or \
       ((board[0][0] == "T" or board[0][0] == "X") and
       (board[1][2] == "T" or board[1][1] == "X") and
       (board[2][2] == "T" or board[2][2] == "X") and
       (board[3][3] == "T" or board[3][3] == "X")) or \
       ((board[0][3] == "T" or board[0][3] == "X") and
       (board[1][2] == "T" or board[1][2] == "X") and
       (board[2][1] == "T" or board[2][1] == "X") and
       (board[3][0] == "T" or board[3][0] == "X"))
    
    OWon =  ((board[0][0] == "T" or board[0][0] == "O") and
       (board[0][1] == "T" or board[0][1] == "O") and
       (board[0][2] == "T" or board[0][2] == "O") and
       (board[0][3] == "T" or board[0][3] == "O")) or \
       ((board[1][0] == "T" or board[1][0] == "O") and
       (board[1][1] == "T" or board[1][1] == "O") and
       (board[1][2] == "T" or board[1][2] == "O") and
       (board[1][3] == "T" or board[1][3] == "O")) or \
       ((board[2][0] == "T" or board[2][0] == "O") and
       (board[2][1] == "T" or board[2][1] == "O") and
       (board[2][2] == "T" or board[2][2] == "O") and
       (board[2][3] == "T" or board[2][3] == "O")) or \
       ((board[3][0] == "T" or board[3][0] == "O") and
       (board[3][1] == "T" or board[3][1] == "O") and
       (board[3][2] == "T" or board[3][2] == "O") and
       (board[3][3] == "T" or board[3][3] == "O")) or \
       ((board[0][0] == "T" or board[0][0] == "O") and
       (board[1][0] == "T" or board[1][0] == "O") and
       (board[2][0] == "T" or board[2][0] == "O") and
       (board[3][0] == "T" or board[3][0] == "O")) or \
       ((board[0][1] == "T" or board[0][1] == "O") and
       (board[1][1] == "T" or board[1][1] == "O") and
       (board[2][1] == "T" or board[2][1] == "O") and
       (board[3][1] == "T" or board[3][1] == "O")) or \
       ((board[0][2] == "T" or board[0][2] == "O") and
       (board[1][2] == "T" or board[1][2] == "O") and
       (board[2][2] == "T" or board[2][2] == "O") and
       (board[3][2] == "T" or board[3][2] == "O")) or \
       ((board[0][3] == "T" or board[0][3] == "O") and
       (board[1][3] == "T" or board[1][3] == "O") and
       (board[2][3] == "T" or board[2][3] == "O") and
       (board[3][3] == "T" or board[3][3] == "O")) or \
       ((board[0][0] == "T" or board[0][0] == "O") and
       (board[1][2] == "T" or board[1][1] == "O") and
       (board[2][2] == "T" or board[2][2] == "O") and
       (board[3][3] == "T" or board[3][3] == "O")) or \
       ((board[0][3] == "T" or board[0][3] == "O") and
       (board[1][2] == "T" or board[1][2] == "O") and
       (board[2][1] == "T" or board[2][1] == "O") and
       (board[3][0] == "T" or board[3][0] == "O"))
    
    done = True
    for row in board:
        if row.find(".") >= 0:
            done = False
            break
    
    if XWon:
        output.write("Case #" + str(caseNum+1) + ": X won\n")
    elif OWon:
        output.write("Case #" + str(caseNum+1) + ": O won\n")
    elif done:
        output.write("Case #" + str(caseNum+1) + ": Draw\n")
    else:
        output.write("Case #" + str(caseNum+1) + ": Game has not completed\n")
input.close()
output.close()
