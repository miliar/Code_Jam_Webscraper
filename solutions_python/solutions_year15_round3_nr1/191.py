import math
import os
import itertools

for f in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if f.endswith(".in"):
        f_in = open(f)
        f_out = open(f[:-3] + '.out', 'w')

lines = f_in.readlines()
tests = list(map(lambda x: list(map(lambda y: int(y), x.split(' '))), lines[1:]))
d_out = []

for num_test, (R, C, W) in enumerate(tests, 1):
    res = R*int(C/W)
    if (C%W) > 0:
        res += W
    else:
        res += W-1
    d_out.append('Case #' + str(num_test) + ': ' + str(res) + '\n')


f_out.writelines(d_out)
f_out.close()
f_in.close()
