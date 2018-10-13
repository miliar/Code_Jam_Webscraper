import sys

fh = sys.stdin

cases = fh.readline()

def read_board(fh):
    board = []
    for row in range(4):
        board.append(set(fh.readline().split()))
    return board

for case in range(1, int(cases)+1):
    first_row = int(fh.readline())
    first_board = read_board(fh)

    first_candidates = first_board[first_row-1]

    second_row = int(fh.readline())
    second_board = read_board(fh)

    second_candidates = second_board[second_row-1]
    
    answer = first_candidates & second_candidates

    print 'Case #{0}:'.format(case),
    if len(answer) == 1:
        print answer.pop()
    elif len(answer) > 1: 
        print 'Bad magician!'
    else:
        print 'Volunteer cheated!'
