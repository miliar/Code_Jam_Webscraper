import sys, itertools, operator

lines_per_case = 2

def solve_case(case):
    case = map(int, case[1].split())
    
    if wsum(case) != 0:
        return 'NO'
    
    result = -1
    sl = sorted(case, reverse=True)
    for i in range(len(sl)):
        l = wsum(sl[:i])
        r = wsum(sl[i:])
        if l == r:
            result = i
    result = "NO" if result == -1 else str(sum(sl[:i]))
    
    return result

def wsum(l):
    return reduce(operator.xor, l, 0)


def produce_output(index, solution):
    print 'Case #%s: %s' % (index, solution)


def get_test_cases(lines, n_of_lines_per_case=1):
    return itertools.izip(*(iter(lines[i::n_of_lines_per_case] for i in range(n_of_lines_per_case))));

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        fn = sys.argv[1]
        with open(fn) as f:
            lines = f.readlines()
            nt = int(lines[0])
            for index, case in enumerate(get_test_cases(lines[1:], lines_per_case), 1):
                solution = solve_case(case)
                produce_output(index, solution)
            
