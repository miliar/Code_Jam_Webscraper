import os
import sys
import numpy as np
from scipy import linalg
from collections import defaultdict
sys.setrecursionlimit(1999999999)
problem_id = 'B'

sys.setrecursionlimit(10**9)
input_path = '%s.in' % problem_id
output_path = '%s.out' % problem_id


def read_line():
    line = ''
    while len(line) == 0:
        line = input_file.readline().strip()
    return line


def write_line(line):
    print line
    return output_file.write(line + os.linesep)



def solve():
    n, v, x = map(float, read_line().split(' '))
    target = v * x
    n = int(n)
    r = [0] * n
    c = [0] * n
    for i in xrange(n):
        r[i], c[i] = map(float, read_line().split(' '))
    if max(c) < x or min(c) > x:
        return 'IMPOSSIBLE'
    if n == 1:
        return v / r[0]
    if c[0] == c[1]:
        return v / (r[0] + r[1])
    r = np.array(r)
    c = np.array(c)
    return '{0:.9f}'.format(max(np.array([v, v*x]).dot(linalg.inv(np.array([r,np.multiply(r, c)]).T))))



input_file = open(input_path, "r")
output_file = open(output_path, "w+")
T = int(read_line())
for case_id in xrange(1, T + 1):
    write_line("Case #%d: %s" % (case_id, solve()))
input_file.close()
output_file.close()