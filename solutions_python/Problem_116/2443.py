from pprint import pprint
import sys

status = [
    "X won",
    "O won",
    "Draw",
    "Game has not completed",
]

def init_results():
    return {'X': 0, 'O': 0, '.': 0}

def add(results, char):
    if char == 'T':
        results['O'] += 1
        results['X'] += 1
    else:
        results[char] += 1
        
def solve_case(case_counter):
    board = []
    for i in range(4):
        board.append(list(sys.stdin.next().strip()))

    incomplete = False

    for i in range(4):
        col_results, row_results = init_results(), init_results()
        for j in range(4):
            add(row_results, board[i][j])
            add(col_results, board[j][i])

            if row_results['.'] > 0 or col_results['.'] > 0:
                incomplete = True

            if row_results['X'] == 4 or col_results['X'] == 4:
                return 0

            if row_results['O'] == 4 or col_results['O'] == 4:
                return 1

    d1_results, d2_results = init_results(), init_results()
    for i in range(4):
        add(d1_results, board[i][i])
        add(d2_results, board[i][3-i])

        if d1_results['X'] == 4 or d2_results['X'] == 4:
            return 0

        if d1_results['O'] == 4 or d2_results['O'] == 4:
            return 1

    if not incomplete:
        return 2

    return 3

if __name__ == "__main__":
    case_counter = 1
    for line in sys.stdin:
        print "Case #{}: {}".format(
            case_counter,
            status[solve_case(case_counter)])
        case_counter += 1
