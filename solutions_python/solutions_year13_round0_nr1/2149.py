f = open('A-large.in')

raw_input = f.readline
testcases = int(raw_input())

def checker(letter):
    # :)))
    if ((matrix[0][0] == letter or matrix[0][0] == 'T') and
        (matrix[0][1] == letter or matrix[0][1] == 'T') and
        (matrix[0][2] == letter or matrix[0][2] == 'T') and
        (matrix[0][3] == letter or matrix[0][3] == 'T')):
        return '{0} won'.format(letter)

    if ((matrix[1][0] == letter or matrix[1][0] == 'T') and
        (matrix[1][1] == letter or matrix[1][1] == 'T') and
        (matrix[1][2] == letter or matrix[1][2] == 'T') and
        (matrix[1][3] == letter or matrix[1][3] == 'T')):
        return '{0} won'.format(letter)

    if ((matrix[2][0] == letter or matrix[2][0] == 'T') and
        (matrix[2][1] == letter or matrix[2][1] == 'T') and
        (matrix[2][2] == letter or matrix[2][2] == 'T') and
        (matrix[2][3] == letter or matrix[2][3] == 'T')):
        return '{0} won'.format(letter)

    if ((matrix[3][0] == letter or matrix[3][0] == 'T') and
        (matrix[3][1] == letter or matrix[3][1] == 'T') and
        (matrix[3][2] == letter or matrix[3][2] == 'T') and
        (matrix[3][3] == letter or matrix[3][3] == 'T')):
        return '{0} won'.format(letter)

    if ((matrix[0][0] == letter or matrix[0][0] == 'T') and
        (matrix[1][0] == letter or matrix[1][0] == 'T') and
        (matrix[2][0] == letter or matrix[2][0] == 'T') and
        (matrix[3][0] == letter or matrix[3][0] == 'T')):
        return '{0} won'.format(letter)

    if ((matrix[0][1] == letter or matrix[0][1] == 'T') and
        (matrix[1][1] == letter or matrix[1][1] == 'T') and
        (matrix[2][1] == letter or matrix[2][1] == 'T') and
        (matrix[3][1] == letter or matrix[3][1] == 'T')):
        return '{0} won'.format(letter)

    if ((matrix[0][2] == letter or matrix[0][2] == 'T') and
        (matrix[1][2] == letter or matrix[1][2] == 'T') and
        (matrix[2][2] == letter or matrix[2][2] == 'T') and
        (matrix[3][2] == letter or matrix[3][2] == 'T')):
        return '{0} won'.format(letter)

    if ((matrix[0][3] == letter or matrix[0][3] == 'T') and
        (matrix[1][3] == letter or matrix[1][3] == 'T') and
        (matrix[2][3] == letter or matrix[2][3] == 'T') and
        (matrix[3][3] == letter or matrix[3][3] == 'T')):
        return '{0} won'.format(letter)

    if ((matrix[0][0] == letter or matrix[0][0] == 'T') and
        (matrix[1][1] == letter or matrix[1][1] == 'T') and
        (matrix[2][2] == letter or matrix[2][2] == 'T') and
        (matrix[3][3] == letter or matrix[3][3] == 'T')):
        return '{0} won'.format(letter)

    if ((matrix[0][3] == letter or matrix[0][3] == 'T') and
        (matrix[1][2] == letter or matrix[1][2] == 'T') and
        (matrix[2][1] == letter or matrix[2][1] == 'T') and
        (matrix[3][0] == letter or matrix[3][0] == 'T')):
        return '{0} won'.format(letter)

def solver(matrix):
    is_empty_cell = False

    for i in matrix:
        for j in i:
            if j == '.':
                is_empty_cell = True

    check = checker('X')
    if check:
        return check

    check = checker('O')
    if check:
        return check

    if is_empty_cell:
        return 'Game has not completed'

    return 'Draw'

for i in range(testcases):
    matrix = []
    for j in range(4):
        matrix.append([k for k in raw_input()])

    raw_input()
    answer = solver(matrix)
    print('Case #{0}: {1}'.format(i + 1, answer))

