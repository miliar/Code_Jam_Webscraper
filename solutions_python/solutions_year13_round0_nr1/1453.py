

def solve(d):
    d = d[:4]
    cases = d[:]
    for i in range(4):
        cases.append(''.join([line[i] for line in d]))
    cases.append(''.join([line[j] for j, line in enumerate(d)]))
    cases.append(''.join([line[3 - j] for j, line in enumerate(d)]))

    for case in cases:
        if case.count('X') == 4 or (case.count('X') == 3 and 'T' in case):
            return 'X won'
        if case.count('O') == 4 or (case.count('O') == 3 and 'T' in case):
            return 'O won'

    for line in d:
        if '.' in line:
            return 'Game has not completed'

    return 'Draw'


if __name__ == '__main__':
    n = input()
    for i in range(n):
        d = [raw_input() for j in range(5)]
        print 'Case #{}: {}'.format(i + 1, solve(d))
