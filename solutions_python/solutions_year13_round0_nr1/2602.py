

def main():

    lines = open('A-large.in').readlines()
    num_cases = int(lines.pop(0))
    output = open('pa.out', 'w')

    for n in range(num_cases):

        board = []
        board.append(lines.pop(0))
        board.append(lines.pop(0))
        board.append(lines.pop(0))
        board.append(lines.pop(0))
        lines.pop(0)

        result = analyze(board)
        if result == 'X':
            print 'Case #%d: X won' % (n + 1)
            output.write('Case #%d: X won\n' % (n + 1))
        if result == 'O':
            print 'Case #%d: O won' % (n + 1)
            output.write('Case #%d: O won\n' % (n + 1))
        if result == 'd':
            print 'Case #%d: Draw' % (n + 1)
            output.write('Case #%d: Draw\n' % (n + 1))
        if result == 'nc':
            print 'Case #%d: Game has not completed' % (n + 1)
            output.write('Case #%d: Game has not completed\n' % (n + 1))


def analyze(board):

    # horizontal
    for i in range(4):
        line = board[i]
        result = check_win(line)
        if result != '':
            return result

    # vertical
    for i in range(4):
        line = generator_to_string(z[i] for z in board)
        result = check_win(line)
        if result != '':
            return result

    diaga = ''
    for i in range(4):
        diaga += board[i][i]
    result = check_win(diaga)
    if result != '':
        return result

    diagb = ''
    for i in range(4):
        diagb += board[3 - i][i]
    result = check_win(diagb)
    if result != '':
        return result

    if [c for l in board for c in l].count('.') ==  0:
        return 'd'
    return 'nc'


def generator_to_string(gen):

    s = ''
    for c in gen:
        s += c
    return s

def check_win(line):

    if line.count('X') == 4 or line.count('X') == 3 and line.count('T') == 1:
        return 'X'
    if line.count('O') == 4 or line.count('O') == 3 and line.count('T') == 1:
        return 'O'
    return ''

main()
