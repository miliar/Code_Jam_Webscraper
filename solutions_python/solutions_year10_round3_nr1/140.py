from sys import stdin

T = int(stdin.readline())

for j in xrange(T):
   N = int(stdin.readline())
   ropes = []
   for i in xrange(N):
      a, b = map(int, stdin.readline().split(' '))
      ropes.append((a, b))
   count = 0
   for a0, b0 in ropes:
      for a1, b1 in ropes:
         if a0 < a1:
            if b0 > b1:
               count += 1
   print "Case #%s:" % (j+1),
   print count

