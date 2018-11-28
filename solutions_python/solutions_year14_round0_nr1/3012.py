#! /usr/bin/python

import sys, getopt

def get_params(*defaults):
    argv = sys.argv[1:]
    input_problem, input_set, lines_per_case = defaults
    try:
        opts, args = getopt.getopt(argv,"p:s:l:",["problem=", "set=","lines="])
    except getopt.GetoptError:
        print sys.argv[0], '-p <problem letter> -s <input set> -l <lines per case>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print sys.argv[0], '-p <problem letter> -s <input set> -l <lines per case>'
            sys.exit()
        elif opt in ("-p", "--problem"):
            input_problem = arg
        elif opt in ("-s", "--set"):
            input_set = arg
        elif opt in ("-l", "--lines"):
            lines_per_case = int(arg)
    return (input_problem, input_set, lines_per_case)

def iter_cases(input_problem, input_set, lines_per_case):
    in_file = open('%s-%s.in' % (input_problem, input_set), 'r')

    line = in_file.readline()

    count = int(line)
    print count, "cases"

    for i in range(1, count + 1):
        print i,
        if i % 50 == 0: print
        case = [chomp(in_file.readline()) for l in range(lines_per_case)]
        yield case
    print

    in_file.close()
    
def main():
    input_problem, input_set, lines_per_case = get_params('A', 'small-attempt0', 10) 

    out_file = open('%s-%s.out' % (input_problem, input_set), 'w')

    for i, case in enumerate(iter_cases(input_problem, input_set, lines_per_case)):
        solution = solve(case)
        out_file.write('Case #%d: %s\n' % (i+1, solution))

    out_file.close()

def split(line):
    return chomp(line).split(' ')

def chomp(line):
    return line.replace('\n', '')

def solve(case):
    r1, a1, r2, a2 = case[0], case[1:5], case[5], case[6:]
    r1, r2 = int(r1)-1, int(r2)-1
    a1 = [int(x) for x in split(a1[r1])]
    a2 = [int(x) for x in split(a2[r2])]
    
    x = set(a1).intersection(set(a2))
    
    if len(x) == 1:
        return list(x)[0]
    elif len(x) > 1:
        return 'Bad magician!'
    elif len(x) < 1:
        return 'Volunteer cheated!'
    return None

if __name__ == '__main__':
    main()
