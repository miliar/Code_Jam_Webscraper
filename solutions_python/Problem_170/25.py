import os
import sys
from collections import defaultdict
sys.setrecursionlimit(1999999999)
problem_id = 'C'

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

min_count = None
lines = []

def search(x, eng, fre):
    count = len(eng & fre)
    if x == -1:
        global min_count
        if min_count is None or count < min_count:
            min_count = count
        return count
    if min_count is not None and count > min_count:
        return count
    return min(search(x - 1, lines[x] | eng, fre), search(x - 1, eng, lines[x] | fre))


def solve():
    n = int(read_line())
    global lines
    global min_count
    min_count = None
    lines = [set(read_line().split(' ')) for i in xrange(n)]
    eng = lines[0]
    fre = lines[1]
    lines = lines[2:]
    return search(len(lines) - 1, eng, fre)


input_file = open(input_path, "r")
output_file = open(output_path, "w+")
T = int(read_line())
for case_id in xrange(1, T + 1):
    write_line("Case #%d: %s" % (case_id, solve()))
input_file.close()
output_file.close()