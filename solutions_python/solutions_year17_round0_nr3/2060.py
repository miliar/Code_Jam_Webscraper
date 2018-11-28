#!/usr/bin/pythonw
t = int(raw_input())
for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]
  L = 0
  R = 0
  huecos = list()
  huecos.append(n)
  for r in xrange(k):
  	next = max(huecos)
	if (next % 2 == 0):
		L = (next/2)-1
		R = (next/2)
	else:
		L = (next/2)
		R = (next/2)
	huecos.append(L)
	huecos.append(R)
	huecos.remove(next) 
  y = R
  z = L
  print "Case #{}: {} {}".format(i, y, z)