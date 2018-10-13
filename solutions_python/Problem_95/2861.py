import sys

d = {}
def Main():
  G  = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
  E = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give u"

  
  # d is G->E
  for i in xrange(len(G)-1):
    d[G[i]] = E[i]
  d['q'] = 'z'
  d['z'] = 'q'

  F = open(sys.argv[1])
  N = int(F.readline())
  for i in range(N):
    s = F.readline()
    y = ""
    for j in range(len(s)-1):
      y += d[s[j]]
    print "Case #%d: %s" % (i+1, y)

Main()

