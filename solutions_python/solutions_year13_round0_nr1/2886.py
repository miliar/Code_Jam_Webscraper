INPUT_FILENAME = "SampleInput.txt"
OUTPUT_FILENAME = "SampleOuput.txt"

def read_input():
    f = open(INPUT_FILENAME, 'r')
    size = int(f.readline().split()[0])

    all_boards = []
    
    for testcase in range(size):
        board = []
        for line in range(4):
            newline = f.readline()
            board.append(newline[0])
            board.append(newline[1])
            board.append(newline[2])
            board.append(newline[3])
            
            emptyline = f.readline()
            
        
        all_boards.append(board)
        
    f.close()
    return all_boards
    
def read_input_revised():
    f = open(INPUT_FILENAME, 'rU')
    all_lines_bad = f.readlines()
    
    all_lines = all_lines_bad
    for lines in all_lines_bad:
        #all_lines.append(lines.replace("\n", "\r\n"))
        pass
    
    size = int(all_lines[0].split()[0])
    print all_lines
    relevant_lines = all_lines[1:]
    
    all_boards = []
    for testcase in range(size):
        board = []
        for line in range(4):
            newline = relevant_lines[5 * testcase + line]
            board.append(newline[0])
            board.append(newline[1])
            board.append(newline[2])
            board.append(newline[3])
            
        #print len(board)
        all_boards.append(board)
        
    #print all_boards
    return all_boards
 
    
def check_all_boards(all_boards):
    f = open(OUTPUT_FILENAME, 'w')
    #print ("number of boards " + str(len(all_boards)))
    for i, board in enumerate(all_boards, 1):
        #print board
        case = check_case(board)
        f.write("Case #" + str(i) + ": " + case + "\r\n")
        
    f.close()
    
def check_case(board):
    possibilities = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
        [4, 8, 12, 16],
        [1, 6 ,11, 16],
        [4, 7, 10, 13]]
        
        
        
    winX = False
    winO = False
    
    for p in possibilities:
        if check_quad(board, p, 'X'):
            winX = True
    if winX:
        return "X won"
            
    for p in possibilities:
        if check_quad(board, p, 'O'):
            winO = True
            
    if winO:
        return "O won"
        
    else:
        if board.count('.') > 0:
            return "Game has not completed"
        else:
            return "Draw"
            
def check_quad(board, quad, player):
    for cell in quad:
        if (board[cell - 1] != player and board[cell - 1] != 'T'): #-1 because index is without 0
            return False
    return True
    
if __name__ == "__main__":
    all_boards = read_input_revised()
    check_all_boards(all_boards)