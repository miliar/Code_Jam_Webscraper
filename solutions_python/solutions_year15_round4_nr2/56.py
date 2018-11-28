import os
import sys
import numpy as np
from scipy import linalg
from collections import defaultdict

input_path = 'in.txt'
output_path = 'out.txt'

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
    r = [0] * int(n)
    c = [0] * int(n)
    for i in xrange(int(n)):
        r[i], c[i] = map(float, read_line().split(' '))
    if max(c) < x or min(c) > x:
        return 'IMPOSSIBLE'
    elif n == 1:
        return v / r[0]
    elif c[0] == c[1]:
        return v / (r[0] + r[1])
    r = np.array(r)
    c = np.array(c)
	
    target = v * x
    return '{0:.9f}'.format(max(np.array([v, v*x]).dot(linalg.inv(np.array([r,np.multiply(r, c)]).T))))

input_file = open(input_path, "r")
output_file = open(output_path, "w")
T = int(read_line())
for case_id in xrange(1, T + 1):
    write_line("Case #%d: %s" % (case_id, solve()))
input_file.close()
output_file.close()