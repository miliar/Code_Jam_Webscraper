#!/usr/bin/python
import sys
def raw_input(f=open(sys.argv[1])): return f.readline().rstrip()
t = int(raw_input())
for i in range(t):
   s, k = raw_input().split()
   s = list(s)
   k = int(k)
   f = 0
   for j in range(len(s)):
      if s[j] == '-':
         if j > len(s)-k:
            f = -1
            break
         f += 1
         for m in range(k):
            if s[j+m] == '-':
               s[j+m] = '+'
            else:
               s[j+m] = '-'
   print 'Case #%d: %s' % (i+1, 'IMPOSSIBLE' if f < 0 else str(f))

