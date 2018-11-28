import sys
from math import ceil
lines = open(sys.argv[1] + ".in", "rU").read().split("\n")

outfile = open(sys.argv[1] + ".out", "w")

for k, test in enumerate(lines[2::2]):
    test = list(map(int, test.split()))
    results = [0] * (max(test) + 1)
    for p in test:
        for i in range(1, len(results)):
            results[i] += ceil(p / i) - 1
    results = [i + j for i, j in enumerate(results)]
    print("Case #{}: {}".format(k+1, min(results[1:])), file=outfile)
