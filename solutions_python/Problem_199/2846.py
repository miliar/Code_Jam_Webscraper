import argparse
import shutil
import math, re

parser = argparse.ArgumentParser()
parser.add_argument('problem',  help='Problem name')
parser.add_argument('suffix',  help='Type')
args = parser.parse_args()

problem_name = args.problem
problem_type = args.suffix

input_path = "{}-{}.in".format(problem_name, problem_type)
output_path = "{}-{}.out".format(problem_name, problem_type)
code_path = "{}.py".format(problem_name)

with open(input_path, 'r') as in_file, open(output_path, 'w') as out_file:
    cases = int(in_file.readline().strip())

    for c in range(cases):
        def parse_case():
            def line():
                return in_file.readline().strip()

            def tokens():
                return line().split(" ")

            def ints():
                return map(int, tokens())

            # Read case input
            s, n = tokens()
            return [0 if x == "-" else 1 for x in s], int(n)

        def output(res):
            case_solution = 'Case #{}: {}'.format(c+1, res)
            out_file.write(case_solution)
            out_file.write('\n')
            print(case_solution)

        pancakes, size = parse_case()

        def solve(p, s):
            i = 0
            c = 0
            while i <= len(p)-s:
                if p[i] == 0:
                    c += 1
                    for j in range(s):
                        p[i+j] = 1 - p[i+j]
                i += 1

            if 0 in p:
                return 'IMPOSSIBLE'
            else:
                return c

        output(solve(pancakes, size))


shutil.copyfile('gcj.py', code_path)
