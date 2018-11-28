# task = 'B-sample'
# task = 'B-small-attempt0'
task = 'B-large'

testCaseSpec = '''
#N #M
*N*lines* ##a
'''

possible   = 'YES'
impossible = 'NO'

def solve(N, M, lines):
    lines = [line['a'] for line in lines]

    for i, line in enumerate(lines):
        for j, field in enumerate(line):
            # todo O(n^3)
            if field < max(line) and field < max(line[j] for line in lines):
                return impossible

    return possible

from template import Solver

Solver(task, testCaseSpec, solve).solve()

