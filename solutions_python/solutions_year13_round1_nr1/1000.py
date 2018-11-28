import operator

import math
import sys
# 1, 4, 9, 16, 25, 36, 49
#   3    7     11   15 19
# (n+1+n)(n+1-n)
#   8, 16, 44
# x -> (a + 2(x-1))*x  <= t
# 2x^2 + (a-2)x - t <= 0
# x = (2-a+sqrt((a-2)^2+4*2*t))/4  -- floor
def max_rings(r, t):
    r = float(r)
    t = float(t)
    start = 2*r + 1
    b = start-2

    #print (0-b+math.sqrt(math.pow(b,2)+8*t))/4
    return int(math.floor((0-b+math.sqrt(math.pow(b,2)+8*t))/4))

# read
def file_read(input_file, output_file):
    with open(input_file, "r") as fin:
        with open(output_file, "w") as fout:
            num_test_cases = int(fin.readline())
            for i in range(num_test_cases):
                (r, t) = (int(param) for param in fin.readline().rstrip().split())
                msg = max_rings(r, t)
                fout.write("Case #{num}: {msg}\n".format(num=i+1, msg=msg))


file_read("A-small-attempt0 (1).in", "out_aaa.txt")