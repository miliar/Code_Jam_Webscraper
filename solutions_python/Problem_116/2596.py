def gen_tests(board):
    tests = []
    for i in range(4):
        tests.append(board[i])
    for i in range(4):
        tests.append([])
        for j in range(4):
            tests[len(tests) - 1].append(board[j][i])
    diagonal1 = []
    for i in range(4):
        diagonal1.append(board[i][i])
    tests.append(diagonal1)
    diagonal2 = []
    for i in range(4):
        diagonal2.append(board[i][3-i])
    tests.append(diagonal2)
    return tests

def process_line(line,c):
    if (line.count(c) == 3 and line.count('T') == 1) or line.count(c) == 4:
        return 1
    return 0
    
def process_board(board):
    tests = gen_tests(board)
    xwins = max(process_line(tests [i],"X") for i in range(len(tests)) )
    owins = max(process_line(tests [i],"O") for i in range(len(tests)) )
    if xwins and owins:
        return "Draw"
    if xwins:
        return "X won"
    if owins:
        return "O won"
    for line in board:
        for c in line:
            if c == ".":
                return "Game has not completed"
    return "Draw"
    
    
fInput = file('1.txt',"r")
fOutput = open('results.txt','w')
T = int(fInput.readline())
for i in range(T):
    board = [fInput.readline().rstrip('\n') for k in range(5)][:-1]
    fOutput.write("Case #%s: %s\n" % (i+1,process_board(board)) )


fOutput.close()

