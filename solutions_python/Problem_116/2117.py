import sys
import os

class Symbols:
    X = 'X'
    O = 'O'
    JOKER = 'T'
    EMPTY = '.'

class Outputs:
    X_WON = 'X won'
    O_WON = 'O won'
    DRAW = 'Draw'
    NOT_COMPLETED = 'Game has not completed'


def _check_symbol_row(symbol, state_repr):
    for row in state_repr:
        if all([element == symbol or element == Symbols.JOKER for element in row]):
            return True
    return False
    
def _check_symbol_column(symbol, state_repr):
    columns = ['', '', '', '']
    for row in state_repr:
        for index in range(len(row)):
            columns[index] = '%s%s' % (columns[index], row[index], )
    return _check_symbol_row(symbol, columns)
    
def _check_symbol_diagonal(symbol, state_repr):
    diagonals = [ ''.join([state_repr[i][i] for i in range(len(state_repr))]),
                        ''.join([state_repr[i][len(state_repr)-i-1] for i in range(len(state_repr))]), ]
    return _check_symbol_row(symbol, diagonals)
    
def has_symbol_won(symbol, state_repr):
    return (_check_symbol_row(symbol, state_repr) or 
                _check_symbol_column(symbol, state_repr) or 
                _check_symbol_diagonal(symbol, state_repr))
    
def is_board_full(state_repr):
    return all(element != Symbols.EMPTY for element in ''.join(state_repr))

def process_state(state_repr):
    if has_symbol_won(Symbols.X, state_repr):
        return Outputs.X_WON
    elif has_symbol_won(Symbols.O, state_repr):
        return Outputs.O_WON
    else:
        if is_board_full(state_repr):
            return Outputs.DRAW
        else:
            return Outputs.NOT_COMPLETED
    
def main(args):
    filename = args[0]
    with open(filename, 'rb') as f:
        contents = f.readlines()
    output_filename = 'tic_out.txt'
    f_out = open(output_filename, 'wb')
    
    test_cases_count = int(contents[0].strip())
    splitted_input = ''.join(contents[1:]).split('\n\n')
    print splitted_input
    for index, case in enumerate(splitted_input):
        if not case:
            continue
        # Get the ['OXXX', 'XO..', '..O.', '...O'] representation
        state_repr = case.strip().split()
        state_result = process_state(state_repr)
        
        result_string = 'Case #%d: %s' % (index + 1, state_result)
        if index + 1 != test_cases_count:
            result_string += '\n'
            
        print result_string
        f_out.write(result_string)
        
    f_out.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print 'USAGE'
        
        
        
        