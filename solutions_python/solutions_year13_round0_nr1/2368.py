##############################################################
#   ArkadioG @ Google CodeJam 2013
#
#   This is solution for problem Fair & Square
#   Solution using pypy 1.9
#
#   Large input 1
##############################################################
from datetime import datetime
from math import sqrt

start_work = datetime.now()


# opening input file
print "Opening input file..."
inpath = "abig.in"
inFile = open(inpath, 'r')

# ask for data - number of test cases
N = int(inFile.readline().rstrip() )
print N, "lines of text in file"
cases = [] # list of testcases

# add N testcases to list
print "Adding lines to list"

lines = (N * 5) + 1
table = []
grid = 1
for i in range(lines):
    #~ testCase = raw_input("test case #")
    testCase = inFile.readline().rstrip()
    #~ print testCase
    if testCase != '':
        table.append(testCase)
        if len(table) == 4:
            cases.append(table)
            table = []

# close file
inFile.close()
##################################################################
### Let's now compute
start_code_time = datetime.now()
# Possible outputs:
x_won = "X won"
o_won = "O won"
draw = "Draw"
in_play = "Game has not completed"

# list holding answers about each table
answer = []

# check every board
for board in cases:
    empty_fields = False
    # 0 if no answer found, 1 if board got answer
    board_state = 0

    # look in diagonals
    # top left to bottom right
    os = 0
    xs = 0
    ts = 0
    for i in range(0, 4):
        if board[i][i] == 'X':
            xs += 1
        elif board[i][i] == 'O':
            os += 1
        elif board[i][i] == 'T':
            ts += 1
        elif board[i][i] == '.':
            empty_fields = True

    if xs + ts == 4:
        answer.append(x_won)
        board_state = 1
    elif os + ts == 4:
        answer.append(o_won)
        board_state = 1


    if board_state == 0:
        #top right to bottom left - 3 is max index for field
        os = 0
        xs = 0
        ts = 0
        for i in range(0, 4):
            if board[i][3 - i] == 'X':
                xs += 1
            elif board[i][3 - i] == 'O':
                os += 1
            elif board[i][3 - i] == 'T':
                ts += 1
            elif board[i][3 - i] == '.':
                empty_fields = True

        if xs + ts == 4:
            answer.append(x_won)
            board_state = 1
        elif os + ts == 4:
            answer.append(o_won)
            board_state = 1

    if board_state == 0:
        # look in grids
        for grid in board:
            xs = 0
            os = 0
            ts = 0
            for field in grid:
                if field == 'X':
                    xs += 1
                elif field == 'O':
                    os += 1
                elif field == 'T':
                    ts += 1
                else:
                    empty_fields = True

            if xs + ts == 4:
                answer.append(x_won)
                board_state = 1
            elif os + ts == 4:
                answer.append(o_won)
                board_state = 1

    if board_state == 0:
        # look in columns
        for k in range(0, 4):
            x = 0
            o = 0
            t = 0
            for l in xrange(0, 4):
                if board[l][k] == 'X':
                    x += 1
                elif board[l][k] == 'O':
                    o += 1
                elif board[l][k] == 'T':
                    t += 1
                elif board[l][k] == '.':
                    empty_fields = True

            if x + t == 4:
                answer.append(x_won)
                board_state = 1
            elif o + t == 4:
                answer.append(o_won)
                board_state = 1

    if board_state == 0 and empty_fields == True:
        answer.append(in_play)
    elif board_state == 0 and empty_fields == False:
        answer.append(draw)

end_code_time = datetime.now()

# End calculations - write to file
##########################################################
#~ # open / create file to print in it results
outpath = "abig.out"
outFile = open(outpath, 'w')
print "Creating output file:", outpath

# printout cases to file - one at each line
case = 1                        # number of case
# move along every element of reversed list and print it in lines
print "Writing data into file..."
for i in answer:
    line = "Case #" + str(case) + ":" + " " + str(i) + "\n"  #add \n to start next line
    outFile.write(line)
    case += 1
outFile.close()
print "Finished"                    # all ok
#~ #~
end_work = datetime.now()
print "Working time:", (end_work - start_work)
print "Without file operations time:", (end_code_time - start_code_time)
print "File operations took:", (end_work - start_work) - (end_code_time - start_code_time)
