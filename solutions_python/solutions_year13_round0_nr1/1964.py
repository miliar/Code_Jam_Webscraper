# GCJ 2013 Qualification Round
# Tic-Tac-Toe-Tomek
# A Tic-Tac-Toe-Tomek grid is a 4x4 square (unlike 3x3 for regular
# Tic-Tac-Toe). One 'T' character can occupy one of the 16 squares in
# the grid. After a player's move, if there is a row, col, or diagonal
# containing 4 in a row or 3 in a row plus the char 'T', that player
# wins.
#
# Given a 4x4 board description containing 'X', 'O', 'T' and '.' chars
# (where '.' represents an empty square), describing the current state
# of a game, determine the status of the Tic-Tac-Toe-Tomek game going
# on. The 4 status are "X won", "O won", "Draw", and "Game has not
# completed".

FILE_NAME = "A-large.in"
OUTPUT = "tttt_large.out"

def load_file():
    '''open text file and insert each line into a list'''
    in_file = open(FILE_NAME, 'r', 0)
    line_list = list(in_file)
    in_file.close()
    # remove all newline chars from the list of strings
    line_list = [i.strip('\n') for i in line_list]
    #print line_list
    # remove all elements from line_list that are blank ('')
    line_list = [line_list[i] for i in range(len(line_list))
                if line_list[i] != '']
    #print line_list
    # convert each char of str elems into elems of sublists
    line_list = [list(line_list[i]) for i in range(len(line_list))]
    #print line_list
    return line_list

input_list = load_file()
output_file = open(OUTPUT, 'w')
num_cases = int(''.join(input_list.pop(0))) # remove first index
case_cnt = 1

for case in range(0, num_cases * 4, 4):
    row1 = (input_list[case][0] + input_list[case][1] +
            input_list[case][2] + input_list[case][3])
    row2 = (input_list[(case)+1][0] + input_list[(case)+1][1] +
            input_list[(case)+1][2] + input_list[(case)+1][3])
    row3 = (input_list[(case)+2][0] + input_list[(case)+2][1] +
            input_list[(case)+2][2] + input_list[(case)+2][3])
    row4 = (input_list[(case)+3][0] + input_list[(case)+3][1] +
            input_list[(case)+3][2] + input_list[(case)+3][3])
    col1 = (input_list[(case)][0] + input_list[(case)+1][0] +
            input_list[(case)+2][0] + input_list[(case)+3][0])
    col2 = (input_list[(case)][1] + input_list[(case)+1][1] +
            input_list[(case)+2][1] + input_list[(case)+3][1])
    col3 = (input_list[(case)][2] + input_list[(case)+1][2] +
            input_list[(case)+2][2] + input_list[(case)+3][2])
    col4 = (input_list[(case)][3] + input_list[(case)+1][3] +
            input_list[(case)+2][3] + input_list[(case)+3][3])
    diag1 = (input_list[(case)][0] + input_list[(case)+1][1] +
            input_list[(case)+2][2] + input_list[(case)+3][3])
    diag2 = (input_list[(case)][3] + input_list[(case)+1][2] +
            input_list[(case)+2][1] + input_list[(case)+3][0])
    # create temporary list to store row, cols, diag
    temp_list = []
    temp_list.append(row1)
    temp_list.append(row2)
    temp_list.append(row3)
    temp_list.append(row4)
    temp_list.append(col1)
    temp_list.append(col2)
    temp_list.append(col3)
    temp_list.append(col4)
    temp_list.append(diag1)
    temp_list.append(diag2)
    # logic
    dot_flag = False
    for i in range(len(temp_list)):
        if '.' in temp_list[i]:
            dot_flag = True
    if ('XXXX' in temp_list or 'TXXX' in temp_list or 'XTXX' in
        temp_list or 'XXTX' in temp_list or 'XXXT' in temp_list):
        output_file.write('Case #' + str(case_cnt) + ': ' +
            'X won'+ '\n')
    elif ('OOOO' in temp_list or 'TOOO' in temp_list or 'OTOO' in
        temp_list or 'OOTO' in temp_list or 'OOOT' in temp_list):
        output_file.write('Case #' + str(case_cnt) + ': ' +
            'O won'+ '\n')
    elif dot_flag: # if there is '.' in any 10 str's, game not complete
        output_file.write('Case #' + str(case_cnt) + ': ' +
                'Game has not completed'+ '\n')
    else:
        output_file.write('Case #' + str(case_cnt) + ': ' +
            'Draw'+ '\n')
    case_cnt += 1
output_file.close()
