# Problem from Google Code Jam 2009

import sys
import re

file = open(sys.argv[1])
numbers = map(int, file.readline().split())
words = []
for word in range(numbers[1]):
    words.append(file.readline().strip())
for case in range(1, numbers[2]+1):
    pattern = file.readline().strip().replace('(','[').replace(')',']')
    res = sum(bool(re.match(pattern, word)) for word in words)
    print 'Case #%d: %s' % (case, res)
