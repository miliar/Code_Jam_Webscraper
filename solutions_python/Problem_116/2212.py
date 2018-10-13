SIZE = 4

import sys

def mark_down (new_char, old_char):
    if new_char == '.':
        complete[current_case] = False
        return 'Z'

    if old_char == ' ':
        return new_char
    
    if new_char == 'T' or old_char == new_char:
        return old_char
        
    if old_char == 'T':
        return new_char
        
    else:
        return 'Z'    
      
def process_square (row, col):
    square = all_rows[row][col]
    row_chars[row] = mark_down (square, row_chars[row])
    col_chars[col] = mark_down (square, col_chars[col])
    
    if row == col:
        diag_chars[0] = mark_down (square, diag_chars[0])
    elif row + col == SIZE - 1:
        diag_chars[1] = mark_down (square, diag_chars[1])
      
def get_result (input):
    global row_chars
    global col_chars
    global diag_chars
    global all_rows
    all_rows = input

    row_chars = [' ', ' ', ' ', ' ']
    col_chars = [' ', ' ', ' ', ' ']
    diag_chars = [' ', ' ']
    
    process_square (0, 0)
    process_square (2, 2)
    process_square (1, 1)
    process_square (3, 3)
    
    if diag_chars[0] == 'O' or diag_chars[0] == 'X':
        return diag_chars[0] + " won"
    
    process_square (1, 2)
    process_square (2, 1)
    process_square (0, 3)
    process_square (3, 0)
    
    if diag_chars[1] == 'O' or diag_chars[1] == 'X':
        return diag_chars[1] + " won"
        
    process_square (0, 1)
    process_square (0, 2)  
    
    if row_chars[0] == 'O' or row_chars[0] == 'X':
        return row_chars[0] + " won"

    process_square (1, 0)
    process_square (1, 3)  
    
    if row_chars[1] == 'O' or row_chars[1] == 'X':
        return row_chars[1] + " won"
    
    process_square (2, 0)
    process_square (2, 3)  
    
    if row_chars[2] == 'O' or row_chars[2] == 'X':
        return row_chars[2] + " won"
    if col_chars[0] == 'O' or col_chars[0] == 'X':
        return col_chars[0] + " won"
    if col_chars[3] == 'O' or col_chars[3] == 'X':
        return col_chars[3] + " won"
        
    process_square (3, 1)
    process_square (3, 2)  
    
    if row_chars[3] == 'O' or row_chars[3] == 'X':
        return row_chars[3] + " won"
    if col_chars[1] == 'O' or col_chars[1] == 'X':
        return col_chars[1] + " won"
    if col_chars[2] == 'O' or col_chars[2] == 'X':
        return col_chars[2] + " won"
    
    if complete[current_case]:
        return "Draw"
    else:
        return "Game has not completed"
    
    print row_chars
    print col_chars
    print diag_chars

def get_input (lines):
    result = []
    for line_no in xrange (0, lines):
        result.append(raw_input())
    return result

global current_case
global complete
complete = []
all_input = []

test_cases = int (raw_input())

for test_case in xrange (0, test_cases):
    complete.append(True)
    all_input.append(get_input (SIZE))
    newline = raw_input()

for test_case in xrange (0, test_cases):   
    current_case = test_case
    print "Case #" + str(test_case + 1) + ": " + get_result (all_input[test_case])
