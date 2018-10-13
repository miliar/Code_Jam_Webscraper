from __future__ import with_statement
import re

#FILE = 'A-test.in'
#FILE = 'A-small-attempt0.in'
FILE = 'A-large.in'

with file(FILE, 'r') as f:
    L, D, N = map(int, f.readline().strip().split(' '))

    words = []
    for i in range(D):
        words.append(f.readline().strip())

    testCase = 0
    for testCase in range(1, N + 1):
        pattern = f.readline().strip()
        pattern = pattern.replace("(", "[").replace(")", "]")

        num = 0
        for word in words:
            if re.match(pattern, word):
                num += 1
        
        print "Case #%d: %d" % (testCase, num)
