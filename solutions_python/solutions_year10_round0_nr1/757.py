

numCases = int(raw_input())
for i in xrange(numCases):
   n, k = map(int, raw_input().split())
   if (k+1) % (2**(n)) == 0:
      print "Case #%d: ON" % (i+1)
   else:
      print "Case #%d: OFF" % (i+1)

