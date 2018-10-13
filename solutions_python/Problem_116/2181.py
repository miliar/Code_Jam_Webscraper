import time

def find(first,second,third,forth):
    n = first
    first = list(first[:-1])    # split each character to a list
    second = list(second[:-1])  # split each character to a list
    third = list(third[:-1])    # split each character to a list
    forth = list(forth[:-1])    # split each character to a list
    
    board = [[] for i in range(4)]  # create board from 2D list
    board[0] = first                # first row
    board[1] = second               # second row
    board[2] = third                # third row
    board[3] = forth                # forth row

    if isWinner(board,'O'):
        return "O won"
    elif isWinner(board,'X'):
        return "X won"
    elif any('.' in i for i in board):
        return "Game has not completed"
    else:
        return "Draw"
    
   
    return "test"


def isWinner(board,turn):
    return ((board[0][0] in (turn,'T') and board[0][1] in (turn,'T') and board[0][2] in (turn,'T') and board[0][3] in (turn,'T')) or  # 1st top horizontal
            (board[1][0] in (turn,'T') and board[1][1] in (turn,'T') and board[1][2] in (turn,'T') and board[1][3] in (turn,'T')) or  # 2nd top horizontal
            (board[2][0] in (turn,'T') and board[2][1] in (turn,'T') and board[2][2] in (turn,'T') and board[2][3] in (turn,'T')) or  # 3rd top horizontal
            (board[3][0] in (turn,'T') and board[3][1] in (turn,'T') and board[3][2] in (turn,'T') and board[3][3] in (turn,'T')) or  # 3rd top horizontal

            (board[0][0] in (turn,'T') and board[1][0] in (turn,'T') and board[2][0] in (turn,'T') and board[3][0] in (turn,'T')) or  # 1st left vertical
            (board[0][1] in (turn,'T') and board[1][1] in (turn,'T') and board[2][1] in (turn,'T') and board[3][1] in (turn,'T')) or  # 2nd left vertical
            (board[0][2] in (turn,'T') and board[1][2] in (turn,'T') and board[2][2] in (turn,'T') and board[3][2] in (turn,'T')) or  # 3rd left vertical
            (board[0][3] in (turn,'T') and board[1][3] in (turn,'T') and board[2][3] in (turn,'T') and board[3][3] in (turn,'T')) or  # 3rd left vertical
    
            (board[0][0] in (turn,'T') and board[1][1] in (turn,'T') and board[2][2] in (turn,'T') and board[3][3] in (turn,'T')) or  # diagonal right
            (board[0][3] in (turn,'T') and board[1][2] in (turn,'T') and board[2][1] in (turn,'T') and board[3][0] in (turn,'T'))     # diagonal left
            )

start_time = time.time()
infile = open('A-large.in','r') # open input file
output_file = open("output.txt", "w") # open output file

t = int(infile.readline())  # read number of test case

testcase = 1

for first in infile: # start from the second line
    second = infile.next()
    third = infile.next()
    forth = infile.next()
    empty = infile.next()
    
    output_file.write("Case #" + str(testcase) + ": " + str(find(first,second,third,forth))+"\n")
    testcase+=1



infile.close() # close input file
output_file.close() # close output file
print time.time() - start_time, "seconds"
