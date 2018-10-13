import sys
import re

"""
Tic-Tac-Toe-Tomek
Played on a 4x4 square board (16 squares)
board starts empty except for a single T symbol in 1 the squares
Two players: X and O
Win on 4 of a person's symbols, or 3 of their symbols and the T

Board description: 'X' 'O' 'T' or '.' (empty space) characters
statuses: 

Input:
    line1: the number of test cases
    each test case is 4 lines with 4 characters each
    each test case followed by an empty line
Output:
    For each test case, output one line containing "Case #x: y"
    where x is the case number (starting from 1) and y is one of the statuses
"""

T = 'T'
X = 'X'
O = 'O'
DOT = '.'
X_WON = "X won"
O_WON = "O won"
WINNER = {X: X_WON, O: O_WON}
DRAW = "Draw"
NC = "Game has not completed"
TEST_CASE_PATTERN = re.compile(r'')

########

def parse_number_of_test_cases(text):
    number, text = text.split('\n', 1)
    return int(number), text

def parse_text_into_separate_test_cases(text):
    """
    Iterator that outputs one complete test case chunk per

    """    
    for test_case in text.split('\n\n'):
        yield test_case
    #for test_case in TEST_CASE_PATTERN.finditer(text):
        #yield test_case.group(0)

def parse_test_case(text):
    """
    Generator that produces 1 output grid per iteration.
    
    @param text: (str) the input file text
    
    @returns: (list of list of str) a list of 10 lists, where each list
        is a list of 4 player inputs that represents a column, row, or diagonal
    """
    rows = [list(item) for item in text.split('\n')]
    columns = [[], [], [], []]
    diagonals = [[], []]
    for i in range(4):
        for j in range(4):
            columns[j].append(rows[i][j])
            if i == j:
                diagonals[0].append(rows[i][j])
            if (i, j) in [(0, 3), (1, 2), (2, 1), (3, 0)]:
                diagonals[1].append(rows[i][j])
    return rows + columns + diagonals

def format_output(output, case_number, status):
    """
    Format and properly append the output for the given
    case number and status.
    """
    output.append("Case #%s: %s" % (case_number, status))

def solve(grid):
    """
    """
    complete = True
    for row in grid:
        current = row[0]
        score = 1
        for item in row[1:]:
            if item == DOT:
                complete = False
                break
            elif item == T:
                score += 1
            elif item == current:
                score += 1
            else:
                break
        if score == 4:
            return WINNER[current]
    if not complete:
        return NC
    else:
        return DRAW

def print_final_output(output):
    for line in output:
        print line

def main(text):
    test_cases, text = parse_number_of_test_cases(text)
    output = []
    case_number = 1
    for test_case in parse_text_into_separate_test_cases(text):
        if not test_case:
            continue
        grid = parse_test_case(test_case)
        result = solve(grid)
        format_output(output, case_number, result)
        case_number += 1
    print_final_output(output)

if __name__ == "__main__":
    main(sys.stdin.read())
