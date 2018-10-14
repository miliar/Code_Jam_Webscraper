import sys, itertools

lines_per_case = 2

def solve_case(case):
    size = map(int, case[0].split())[0];
    motes = sorted(map(int, case[1].split()))
    l = len(motes)
    print size, motes

    if size == 1 and motes[0] > 0:
        return str(l)

    return str(n_ops(size, motes))


def n_ops(size, motes):
    # how many to the next one?
    ops = 0
    m = motes[0]
    while size <= m:
        size += size -1
        ops += 1
    size += motes[0]

    l = len(motes)
    if l > 1:
        return min(ops + n_ops(size, motes[1:]), len(motes))
    else:
        return min(ops, 1)

def produce_output(index, solution):
    print 'Case #%s: %s' % (index, solution)


def get_test_cases(lines, n_of_lines_per_case=1):
    x = 0
    while x < len(lines):
        y = x + n_of_lines_per_case
        yield lines[x:y]
        x = y

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        fn = sys.argv[1]
        with open(fn) as f:
            lines = f.readlines()
            nt = int(lines[0])
            for index, case in enumerate(get_test_cases(lines[1:], lines_per_case), 1):
                solution = solve_case(case)
                produce_output(index, solution)
