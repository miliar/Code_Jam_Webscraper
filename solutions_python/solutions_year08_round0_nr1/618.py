def readInput(inf, out):
   fin = open(inf, 'r')
   fout = open(out, 'w')
   cases = fin.readline().strip()
   for i in range(1, int(cases) + 1):
      s = fin.readline().strip()
      searches = [fin.readline().strip() for x in range(int(s))]
      q = fin.readline().strip()
      queries = [fin.readline().strip() for x in range(int(q))]
      fout.write( "Case #%d: %s\n" % (i, minSwitches(searches, queries)) )


def minSwitches(s, q):
   if not len(q):
      return 0
   qunique = [x for x in orderedSet(q) if (x in s)]
   qset = set(qunique)
   sset = set(s)
   if len(sset.difference(qset)):
      return 0 
   return 1 + minSwitches(s, q[q.index(qunique[-1]):])

def orderedSet(n):
   r = []
   [r.append(x) for x in n if not (x in r)]
   return r

readInput('A-small-attempt1.in', 'A-small-attempt1.out')