import sys
from pprint import pprint as pp

X = 'X'
O = 'O'
T = 'T'
DOT = '.'

def read_input():
    f = open(sys.argv[1], 'rt')
    count = int(f.readline())

    inputs = []
    for c in xrange(count):
        matrix = []
        for x in xrange(4):
            line = f.readline()
            matrix.append([line[0], line[1], line[2], line[3]])
        f.readline()
        inputs.append(matrix)
    f.close()
    return inputs

def is_line_won(line, symbol):
    if line.count(symbol) + line.count(T) == 4:
        return True

def is_matrix_won(matrix, symbol):
    won = any([is_line_won(line, symbol) for line in matrix])
    if won:
        return True

    for i in xrange(4):
        line = [matrix[0][i], matrix[1][i], matrix[2][i], matrix[3][i]]
        if is_line_won(line, symbol):
            return True

    if is_line_won([matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3]], symbol):
        return True
    if is_line_won([matrix[0][3], matrix[1][2], matrix[2][1], matrix[3][0]], symbol):
        return True

    return False

def is_game_completed(matrix):
    return 0 == sum([line.count(DOT) for line in matrix])

def main():
    inputs = read_input()

    idx = 1
    for matrix in inputs:
        print 'Case #{}:'.format(idx),

        if is_matrix_won(matrix, X):
            print X, 'won'
        elif is_matrix_won(matrix, O):
            print O, 'won'
        elif is_game_completed(matrix):
            print 'Draw'
        else:
            print 'Game has not completed'
        idx += 1

if __name__ == '__main__':
    main()
