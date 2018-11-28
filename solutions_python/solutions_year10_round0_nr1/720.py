#snapper.py

import sys, re

in_file_name = sys.argv[1]
out_file_name = sys.argv[2]

in_file = open(in_file_name, 'r')
out_file = open(out_file_name, 'w')

first = re.split(' ', in_file.readline())
num_cases = int(first[0])

for i in xrange(num_cases):
    line = re.split(' ', in_file.readline())
    n, k = int(line[0]), int(line[1])
    cycle = 2**n
    if k+1 < cycle or (k+1) % cycle != 0:
        out_file.write("Case #%d: OFF\n" % (i+1))
        continue
    out_file.write("Case #%d: ON\n" % (i+1))

out_file.close()
in_file.close()

