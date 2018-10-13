from __future__ import division
import numpy as np

filen = 'in'
with open(filen) as f:
	content = f.readlines()

content = [i.strip() for i in content]


testn = 1
for line in content[1:]:
	tot = 1
	c,f,x = [float(i) for i in line.split(" ")]
	m = x / 2
	m2 = c / 2
	m1 = x / (2 + f) + m2
	while m > m1:
		m = m1
		m2 = m2 + c / (2 + f * (tot))
		tot += 1
		m1 = x / (2 + f * tot) + m2
		#print m, m1, m2
	print "Case #%d: %f" % (testn, m)
	testn += 1
