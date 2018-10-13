def doCase(r,k,n):
  #r runs, k=ppl, n = irrelevant
  lne = stdin.readline()
  pList = [int(x) for x in lne.split()]
  pList.reverse()
  #print k, pList
  val = 0
  for i in xrange(r):
	added = 0
	cnt2 = 0
	#print 'r', i
	for _ in xrange(len(pList)):
	  if pList[-1]+added > k:
		break
	  c = pList.pop()
	  #print 'c', c
	  added+=c
	  pList.insert(0,c)
	val+=added
  
  return val
  

import sys

stdin = sys.stdin

num = sys.stdin.readline()

#print num

for i in xrange(int(num)):
  f = stdin.readline()
  r,k,n = f.split()
  val = doCase(int(r), int(k), int(n))
  print 'Case #%s: %s' % (i+1, val)