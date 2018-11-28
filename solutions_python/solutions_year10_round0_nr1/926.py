f = open('small.in')
text = f.read()
f.close()
text = text.split('\n')

del(text[len(text)-1])

	

def cont(a):
	if a == 1:
		s = 0
	else:
		s = 1
	return s

def process(n,k,p,q):

	for i in p:
		p[i] = 0
		q[i] = 0

	snap = 1

	while snap <= k:
		for i in range(n):
			if i == 0:
				q[i] = cont(p[i])
			else:
				if i-1 == 0:
					if p[i-1] == 1:
						q[i] = cont(p[i])
					else:
						q[i] = p[i]
				else:
					s = 1
					for j in range(i):
						s = s and p[j]
					if s == 1:
						q[i] = cont(p[i])
					else:
						q[i] = p[i]
					
		for i in range(n):
			p[i] = q[i]
		snap = snap + 1
		
	
	return q


index = 0
for line in text:
	index = index + 1
	n = int(line.split()[0])
	k = int(line.split()[1])
	p = range(n)
	q = range(n)
	result = process(n,k,p,q)

	neutral = 1
	for item in result:
		neutral = neutral and item
	if neutral == 0:
		t = "OFF"
	else:
		t = "ON"
	f = open('small.out','a')
	f.write("Case #%s: %s\n" % (str(index), t))
	f.close()




