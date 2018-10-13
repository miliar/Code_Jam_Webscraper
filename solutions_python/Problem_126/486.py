import sys, itertools, re

lines_per_case = 1

dic = {}

def solve_case(case):
    name, n  = case[0].split()
    pattern = re.compile(r'[^aeiou]{' + n + '}', re.I)
    n = int(n)

    s1 = get_cc(name, int(n), pattern)
    l = len(name)
    i = 1
    s2 = 0
    while l > n:
        cname = name[i:]
        s2 += get_cc(cname, n, pattern)
        i += 1
        l -= 1

    dic[(name, n)] = s1 + s2

    return str(s1 + s2)

def get_cc(name, n, pattern):
    t = (name, n)
    if t in dic:
        return dic[t]

    sc = 0
    if pattern.search(name):
        sc += 1

    if len(name) > n:
        sc += get_cc(name[:-1], n, pattern)

    dic[t] = sc
    return sc

def produce_output(index, solution):
    print 'Case #%s: %s' % (index, solution)


def get_test_cases(lines, n_of_lines_per_case=1):
    x = 0
    while x < len(lines):
        y = x + n_of_lines_per_case
        yield lines[x:y+1]
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
