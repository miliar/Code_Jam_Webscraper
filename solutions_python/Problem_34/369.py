import sys
filename = sys.argv[1]
f = open(filename)
L, D, N = f.readline().split()
words = [f.readline() for i in range(int(D))]
cases = [f.readline() for i in range(int(N))]

import re
def preprocess(case):
  return r'^%s$' % case.replace('(', '[').replace(')', ']')

for n, case in enumerate(cases):
  pattern = preprocess(case)
  count = 0
  for word in words:
    if re.match(pattern, word):
      count += 1
  
  print "Case #%d: %d" % (n+1, count)