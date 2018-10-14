"""

"""

import sys

infile = sys.argv[1]
outfile = sys.argv[2]

test_cases = []
with open(infile, 'r') as f:

    T = int(f.readline()[:-1])
    for _ in range(T):
        D, N = map(int, f.readline()[:-1].split())
        test_case = []
        for _ in range(N):
            Ki, Si = map(int, f.readline()[:-1].split())
            Fi = (D - Ki) / float(Si)
            test_case.append((Ki, Si, Fi))
        test_cases.append((D, test_case))

solutions = []
for D, others in test_cases:

    t_longest = max(others, key=lambda x: x[2])[2]
    solutions.append(D / t_longest)

with open(outfile, 'w') as f:

    t = 1
    for solution in solutions:
        f.write("Case #%d: %.6f\n" % (t, solution))
        t += 1
