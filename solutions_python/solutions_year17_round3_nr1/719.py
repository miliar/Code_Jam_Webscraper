"""

"""

import sys, math

infile = sys.argv[1]
outfile = sys.argv[2]

test_cases = []
with open(infile, 'r') as f:

        T = int(f.readline()[:-1])
        for _ in range(T):
            N, K = map(int, f.readline()[:-1].split())
            pancakes  = []
            for _ in range(N):
                Ri, Hi = map(float, f.readline()[:-1].split())
                pancakes.append((Ri, Hi))
            test_cases.append((N, K, pancakes))

solutions = []
for N, K, pancakes in test_cases:
    base = max(pancakes, key=lambda x: 2 * math.pi * x[0] * x[1] + math.pi * x[0]**2)
    pancakes.remove(base)
    serve = sorted(pancakes, key=lambda x: 2 * math.pi * x[0] * x[1])
    serve = serve[::-1][:K - 1]
    serve.append(base)
    surface = 0.0
    for r, h in serve:
        surface += 2 * math.pi * r * h
    surface += math.pi * max(serve, key=lambda x: x[0])[0]**2
    solutions.append(surface)

t = 1
with open(outfile, 'w') as f:
    for solution in solutions:
        f.write("Case #%d: %.8f\n" % (t, solution))
        t += 1
