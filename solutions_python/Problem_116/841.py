
def check_row(inp, symbol):
    """
    Checks if the given symbol is present continously in any row.
    """
    return any([all([i == symbol or i == 'T' for i in row]) for row in inp])

def check_diagonal(inp, symbol):
    first_diagonal = [inp[0][0], inp[1][1], inp[2][2], inp[3][3]]
    second_diagonal = [inp[3][0], inp[2][1], inp[1][2], inp[0][3]]
    return any([all([i == symbol or i == 'T' for i in diagonal]) for diagonal in [first_diagonal, second_diagonal]])

def check_column(inp, symbol):
    """
    Check if the symbol is continously present in column.
    """
    columns = []
    for i in range(4):
        col_element = ''
        for j in range(4):
            col_element += inp[j][i]
        columns.append(col_element)
    return any([all([i == symbol or i == 'T' for i in col]) for col in columns])

def check_won(inp, symbol):
    """
    Checks if the given symbol is continously present in diagonal or row.
    """
    return any([check_row(inp, symbol), check_diagonal(inp, symbol), check_column(inp, symbol)])

def check_completed(inp, dot='.'):
    """
    if there is a dot in `inp` then the game is not complete.
    """
    return any([dot in row for row in inp])
        

def give_status(inp):
    if check_won(inp, 'X'):
        return "X won"
    elif check_won(inp, 'O'):
        return "O won"
    elif check_completed(inp):
        return "Game has not completed"
    else:
        return "Draw"
    
def read_from_file(filename):
    """ Accepts a filename and parses out the test cases and returns it as list of string.
    """
    inputs = []
    f = open(filename)
    file_content = f.read()
    for line in file_content.split('\n\n'):
        if line:
            inputs.append(line.split('\n'))
    # First element in first row will be the number of test cases, remove it 
    num_of_tests = int(inputs[0][0])
    inputs[0] = inputs[0][1:]
    return inputs

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    inputs = read_from_file(filename)
    for n, inp in enumerate(inputs):
        print "Case #%d: %s" % (n+1, give_status(inp))
