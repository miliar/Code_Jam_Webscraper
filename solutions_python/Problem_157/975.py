import math

def multiply(x,y):
	z = ""
	if x == "1":
		z = y
	elif x == "i":
		if y == "1":
			z = "i"
		elif y == "i":
			z = "-1"
		elif y == "j":
			z = "k"
		elif y == "k":
			z = "-j"
	elif x == "j":
		if y == "1":
			z = "j"
		elif y == "i":
			z = "-k"
		elif y == "j":
			z = "-1"
		elif y == "k":
			z = "i"
	elif x == "k":
		if y == "1":
			z = "k"
		elif y == "i":
			z = "j"
		elif y == "j":
			z = "-i"
		elif y == "k":
			z = "-1"
	return z

def reduse(u):
	if len(u) == 1:
		return u[0]
	else:
		sig = "+"
		z = u[0]
		u.remove(z)
		for c in u:
			z = multiply(z,c)
			if z[0] == '-':
				if sig == '+':
					sig = '-'
				else:
					sig = '+'
				z = z[1]
		if sig == '+':
			return z
		else:
			return '-'+z


f = open("C-small-attempt6.in","r")
out = open("out.txt","w")
n=int(f.readline())

for d in xrange(n):
	l1 = f.readline()
	l1 = l1[:len(l1)-1:]
	l2 = f.readline()
	l2 = l2[:len(l2)-1:]
	l1 = l1.split(" ")
	l2 = l2*int(l1[1])
	bla = []
	for c in l2:
		bla.append(c)
	l2 = bla
	#print len(l2)
	sig = "+"
	phase = 0
	final = "NO"
	if len(l2) > 3:
		i = 1
		x = l2[:len(l2)-2]
		t = 0
		while (t == 0) and (len(x)>1):
			c = x[0]
			x.remove(c)
			c = multiply(c,x[0])

			if c[0] == '-':
				if sig == '+':
					sig = '-'
				else:
					sig = '+'
				c = c[1]
			x[0] = c
			if c == 'i':
				t = 1
			i += 1
		if t == 0:
			i = -1
		#print "i", sig, i


		k = len(l2)-1
		z = l2[2:]
		t = 0
		while (t == 0) and (len(z)>1):
			c = z[len(z)-1]
			z = z[:len(z)-1]
			c = multiply(z[len(z)-1],c)
			if c[0] == '-':
				if sig == '+':
					sig = '-'
				else:
					sig = '+'
				c = c[1]
			z[len(z)-1] = c
			if c == 'k':
				t = 1
			k -= 1
		if t == 0:
			k = -1

		#print "k", sig, k
		if (i != -1) and (k != -1) and (i<k):
			sig = "+"
			x = l2[:i]
			y = l2[i:k]
			z = l2[k:]
			ti = reduse(x)
			tj = reduse(y)
			tk = reduse(z)
			if ti[0] == '-':
				if sig == '+':
					sig = '-'
				else:
					sig = '+'
				ti = ti[1]
			if tj[0] == '-':
				if sig == '+':
					sig = '-'
				else:
					sig = '+'
				tj = tj[1]
			if tk[0] == '-':
				if sig == '+':
					sig = '-'
				else:
					sig = '+'
				tk = tk[1]
			if (ti == "i") and (tj == "j") and (tk == "k") and (sig == "+"):
				final = "YES"
						



	elif len(l2) == 3:
		if (l2[0] == 'i') and (l2[1] == 'j') and (l2[2] == 'k'):
			final = "YES"

			#print "-i-", i, c, len(x)
		
	
	ch = "Case #"+ str(d+1) +": "+ final+"\n"
	print ch[:len(ch)-1]
	out.write(ch)
