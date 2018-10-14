from __future__ import print_function

def parse_input(path):
    with open(path) as fh:
        T = int(fh.readline())
        cases = []
        for i in range(T):
            line = fh.readline()
            S, s = line.split()
            cases.append((S, s))
        return T, cases

def solveCase(case):
    S,s = case
    standing = 0
    friends = 0
    for i in range(len(s)):
        if int(s[i]) != 0:
            if standing >= i:
                standing += int(s[i])
            else:
                friends += (i - standing)
                standing += (i - standing) + int(s[i])
    return friends


def main():
    T, cases = parse_input('inputs/large.txt')
    solutions = []
    for case in cases:
        f = solveCase(case)
        solutions.append(f)
    with open('outputs/output.txt', 'w') as output:
        for i in range(len(solutions)):
            output.write('Case #{}: {}\n'.format(i+1, solutions[i]))

if __name__ == '__main__':
    main()

