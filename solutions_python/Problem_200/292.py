import sys

INPUT_NAME = sys.argv[1]
OUTPUT_NAME = INPUT_NAME.split(".")[0] + ".out"

import numpy as np

f = open(INPUT_NAME,'r')
out = open(OUTPUT_NAME,'w')

num_cases = int(f.readline().strip())

for test in range(num_cases):
    def detract(x):
        return (x+9) % 10
    n = list(map(int,list(f.readline().strip())))
    i = 1
    while i < len(n) and n[i-1] <= n[i]:
        i += 1

    if i != len(n):
        while i > 0 and n[i-1] > n[i]:
            n[i-1] = detract(n[i-1])
            i -= 1

        n = np.array(n)
        n[i+1:] = 9

    out.write("Case #%d: %d\n" % (test+1, int("".join(map(str,n)))))
