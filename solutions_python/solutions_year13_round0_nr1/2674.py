from itertools import combinations

def get_winner(sequence):
    sequence = list(sequence)
    if all (i in 'XT' for i in sequence):
        return 'X'
    if all (i in 'OT' for i in sequence):
        print sequence
        return 'O'

def input():
    with open('a.in') as file:
        tests_count = int(file.readline().strip())
        for i in xrange(tests_count):
            field = []
            for n in xrange(4):
                l = file.readline().strip()
                field.append(l)
            file.readline()
            yield field

def output(results):
    with open('a.out', 'w') as file:
        file.writelines('Case #%s: %s\n' % (i + 1, r) for i, r in enumerate(results))

def solve(input_sequence):
    for field in input_sequence:
        winner = None
        for i in xrange(4):
            winner = get_winner(field[i])
            if winner:
                break
            winner = get_winner(line[i] for line in field)
            if winner:
                break
        if not winner:
            winner = get_winner(field[i][i] for i in xrange(4))
        if not winner:
            winner = get_winner(field[i][3 - i] for i in xrange(4))

        if winner:
            yield '%s won' % winner
        elif any(field[i][j] == '.' for i, j in combinations(range(4), 2)):
            yield 'Game has not completed'
        else:
            yield 'Draw'

if __name__ == '__main__':
    output(solve(input()))