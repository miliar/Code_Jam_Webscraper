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
    input_problem, input_set, lines_per_case = get_params('B', 'large', 1) 

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
    C, F, X = [float(x) for x in split(case[0])]
    rate = 2
    current_best = X / rate
    current_time = 0 
    while (current_time + X / rate) <= current_best:
        current_best = current_time + X / rate
        current_time += C / rate
        rate += F
    return '%.7f' % current_best

if __name__ == '__main__':
    main()
