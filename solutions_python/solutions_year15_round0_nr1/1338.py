
def solve_case(case):
    s_max = case[0]
    series = case[1]

    friends = 0
    standing = 0
    for i in range(len(series)):
        needed = i
        clapper = int(series[i])

        """
        print '---'
        print needed
        print clapper
        print friends
        print standing
        """

        if needed > (standing + friends):
            friends += (needed - standing - friends)

        standing += clapper

    return friends

def parse(input_lines):
    n_cases = int(input_lines.pop(0))
    cases = []

    for i in range(len(input_lines)):
        cases.append(input_lines[i].split(' '))

    return n_cases, cases

def solve(input_file):
    with open(input_file + '.in', 'r') as f:
        input_lines = f.read().split('\n')

    n_cases, cases = parse(input_lines)

    solution = []

    for i in range(0, n_cases):
        answer = solve_case(cases[i])
        solution.append('Case #%s: %s' % (i + 1, answer))

    with open(input_file + '.out', 'w') as f:
        f.write('\n'.join(solution))

if __name__ == '__main__':
    solve('A-large')
    print 'Done!'
