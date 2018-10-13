from sys import stdin

T = int(stdin.readline())

for i in xrange(1, T+1):
   N, K = map(int, stdin.readline().split())
   if K % (2**N) == (2**N-1):
      a = "ON"
   else:
      a = "OFF"
   print "Case #%s: %s" % (i, a)
