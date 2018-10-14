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
            return ints()

        def output(res):
            case_solution = 'Case #{}: {}'.format(c+1, res)
            out_file.write(case_solution)
            out_file.write('\n')
            print(case_solution)


        def solve(n, k):
            while k > 1:
                k, dest = divmod(k, 2)
                if dest == 0:
                    n = int(math.ceil((n-1)/2))
                else:
                    n = (n - 1) // 2

            d, r = divmod(max(n-1, 0), 2)
            return "{} {}".format(d+r, d)


        n, k = parse_case()
        output(solve(n, k))


shutil.copyfile('gcj.py', code_path)
