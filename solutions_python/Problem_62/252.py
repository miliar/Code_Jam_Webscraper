#!/usr/bin/python

t, T = 0, int(raw_input())

while t != T:
   t += 1

   A, B = [], []
   N = int(raw_input())
   for n in xrange(N):
      a, b = map(int, raw_input().split())
      A.append(a)
      B.append(b)

   ans = 0
   for n in xrange(N):
      a = A[n]
      b = B[n]

      for m in xrange(N):
         if (a < A[m] and b > B[m]):
            ans += 1
   
   print 'Case #%d:' % t, ans

