import sys

def is_winning(line, c):
    c_count = line.count(c)
    t_count = line.count('T')
    return c_count + t_count == 4

    
def write_output_file(output_path, outputs):
    
    output_file = open(output_path, 'wb')
    for i, result in enumerate(outputs):
        output_file.write("Case #%d: %s\n" % (i + 1, result))
    output_file.close()

def read_input_file(input_path):

    inputs = []
    input_file = open(input_path, 'rb')
    lines = input_file.readlines()
    test_cases = long(lines[0])
    current_line = 1

    for case in xrange(test_cases):
        inputs.append([lines[j].strip() for j in xrange(current_line, current_line + 4)])
        current_line += 5
    return inputs

def calc_outputs(inputs):
    outputs = []
    for i, board in enumerate(inputs):
        outputs.append(calculate(board))
    return outputs

def calculate(board):
    print '==============='
    if calc_if_palyer_won(board, 'X'):
        return "X won"
    elif calc_if_palyer_won(board, 'O'):
        return "O won"
    elif is_draw(board):
        return "Draw"
    else:
        return "Game has not completed"  
 
def calc_if_palyer_won(board, player_char):
    print board
    
    # calc rows
    for row in board:
        if is_winning(row, player_char):
            return True

    # calc cols
    for col in zip(*board):
        print col
        if is_winning(col, player_char):
            return True

    # calc diagnols
    diags = ([board[i][i] for i in xrange(4)],
            [board[i][3-i] for i in xrange(4)])
    for diag in diags:
        if is_winning(diag, player_char):
            return True

    return False

def is_draw(board):
    return not '.' in ''.join(board)

def main():
    
    input_file = sys.argv[1]
    output_file = sys.argv[1] + ".out"
    
    inputs = read_input_file(input_file)
    outputs = calc_outputs(inputs)
    write_output_file(output_file, outputs)
    

if '__main__' == __name__:
    main()
