
def read_str(lines):
    return lines.next().rstrip('\n')

def read_int(lines):
    return int(lines.next().rstrip('\n'))

def read_strs(lines, length):
    result = []
    for i in xrange(length):
        result.append(lines.next().rstrip('\n'))
    return result

def read_ints(lines, length):
    result = []
    for i in xrange(length):
        result.append(int(lines.next().rstrip('\n')))
    return result

def read_input(input):
    cases = []
    num_cases = read_int(input)
    for i in xrange(num_cases):
        num_engines = read_int(input)
        engines = read_strs(input, num_engines)
        num_searches = read_int(input)
        searches = read_strs(input, num_searches)
        cases.append((engines, searches))
    return cases

def solve(case):
    engines, searches = case
    engines = set(engines)

    solution = []
    engines_left = set(engines)
    while searches:
        search = searches.pop()
        engines_left.discard(search)
        if not engines_left:
            solution.append(search)
            engines_left = set(engines)
            engines_left.discard(search)

    return len(solution)

def main(input, output):
    cases = read_input(input)
    for num, case in enumerate(cases):
        output.write('Case #' + str(num+1) + ': ' + str(solve(case)) + '\n')

if __name__ == '__main__':
    main(open('A-large.in'), open('A-large.out', 'w'))
