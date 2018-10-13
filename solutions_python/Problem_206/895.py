#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import argparse
import shutil
import math, re

parser = argparse.ArgumentParser()
parser.add_argument('problem',  help='Problem name')
parser.add_argument('suffix',  help='Type')
parser.add_argument('-f', '--filter', nargs='+', type=int)
args = parser.parse_args()

problem_name = args.problem
problem_type = args.suffix
cases_filter = args.filter

input_path = "{}-{}.in".format(problem_name, problem_type)
output_path = "{}-{}.out".format(problem_name, problem_type)
code_path = "{}.py".format(problem_name)

with open(input_path, 'r') as in_file, open(output_path, 'w') as out_file:
    cases = int(in_file.readline().strip())

    for c in range(cases):
        def grid_to_str(g):
            return '\n'.join([''.join(str(l)) for l in g])

        def line():
            return in_file.readline().strip()

        def tokens():
            return line().split(" ")

        def ints():
            return map(int, tokens())

        # Read case input
        d, n = ints()
        hs = [tuple(ints()) for i in range(n)]

        if cases_filter is not None and c+1 not in cases_filter:
            continue

        time_left = [(d-h[0])/h[1] for h in hs]
        max_time = max(time_left)

        # print(time_left)
        # print(max_time)

        res = d/max_time

        # Output
        case_solution = 'Case #{}: {}'.format(c + 1, res)
        out_file.write(case_solution)
        out_file.write('\n')
        print(case_solution)


if 'gcj.py' in __file__:
    print("Copied the code to {}".format(code_path))
    shutil.copy('gcj.py', code_path)
