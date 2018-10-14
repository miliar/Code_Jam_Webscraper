#!/usr/bin/python
import sys
import re
def raw_input(f=open(sys.argv[1])): return f.readline().rstrip()
t = int(raw_input())
for i in range(t):
   s = raw_input()
   n = int(s)
   while int(''.join(sorted(list(s)))) != n:
      if re.search(r'^1+0$', s):
         s = re.sub(r'^1+0$', lambda x: '9' * (len(x.group(0))-1), s)
         n = int(s)
      else:
         n -= 1
         s = str(n)
   print 'Case #%d: %d' % (i+1, n)

