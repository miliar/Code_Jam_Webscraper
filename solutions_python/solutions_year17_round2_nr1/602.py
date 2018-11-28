import sys


class Solution:
    def process(self, m, n):
        pass

# INPUT_FILE_NAME = 'input.in'
INPUT_FILE_NAME = 'A-large.in'
OUTOUT_FILE_NAME = 'a-small.out'

fi = open(INPUT_FILE_NAME, 'r')
fo = open(OUTOUT_FILE_NAME, 'w')

number_test = int(fi.readline())
for i in xrange(1, number_test + 1):
    d, n = [int(s) for s in fi.readline().split(" ")]
    max_hours = 0
    for j in range(n):
        start, speed = [int(s) for s in fi.readline().split(" ")]
        rest = (d - start) * 1.0
        if rest / speed > max_hours:
            max_hours = rest / speed
    print i
    fo.write("Case #%s: %s\n" % (i, d/max_hours))

fi.close()
fo.close()
