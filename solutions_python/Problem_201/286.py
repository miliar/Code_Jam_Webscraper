import sys

INPUT_NAME = sys.argv[1]
OUTPUT_NAME = INPUT_NAME.split(".")[0] + ".out"

f = open(INPUT_NAME,'r')
out = open(OUTPUT_NAME,'w')

num_cases = int(f.readline().strip())

import numpy as np

for test in range(num_cases):
    n,k = tuple(map(int, f.readline().strip().split(" ")))
    level = 1
    num_entered = 0
    while k - level > 0:
        k -= level
        num_entered += level
        level *= 2

    lower_bound = (n - num_entered) // (num_entered + 1)
    num_higher = (n - num_entered) % (num_entered + 1)
    ans = lower_bound + (1 if num_higher >= k else 0)

    out.write("Case #%d: %d %d\n" % (test+1, ans//2, (ans-1)//2))
