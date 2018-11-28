import re

f = open('10.in', 'r')
o = open('10.out', 'w')

ldn = f.readline().strip().split(' ')
l = int(ldn[0])

for i in range(l):
	ldn = f.readline().strip().split(' ')
	m = int(ldn[0])
	a = bytes(ldn[1])
	#print m
	total = int(a[0])
	inv = 0
	for j in range(m):
		an = int(a[j+1])
		if an != 0:
			if j+1 > total:
				inv = inv + j+1-total
			total = total + an + inv

	s = "Case #%d: %d\n" % (i+1, inv)
	o.write(s)


'''
dicts = '\n'.join([f.readline().strip() for i in xrange(d)])

for i in xrange(n):
    exp = f.readline().strip()
    exp = exp.replace('(','[').replace(')',']')
    
    r = len(re.findall(exp, dicts))
    
    s = "Case #%d: %s\n" % (i+1, r)
    o.write(s)
'''
f.close()
o.close()
