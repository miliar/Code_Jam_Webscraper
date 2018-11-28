strings = []
answers = []
def xquad(a,b):
	if a == '1':
		return b
	if b == '1':
		return a
	if a[0] == '-' and b[0] =='-':
		a = a[1:]
		b = b[1:]
	if a[0] == '-' or b[0] =='-':
		if a[0] == '-':
			a = a[1:]
			if a[0] == '1':
				return '-'+b
		else:
			b = b[1:]
			if b[0] == '1':
				return '-'+a
		if a[0] == b[0] and a[0]!='1':
			return '1'
		aux = a
		a = b
		b = aux
	if a == b:
		return '-1'
	if a == 'i' and b == 'j':
		return 'k'
	if a == 'j' and b == 'i':
		return '-k'
	if a == 'i' and b == 'k':
		return '-j'
	if a == 'k' and b == 'i':
		return 'j'
	if a == 'j' and b == 'k':
		return 'i'
	if a == 'k' and b == 'j':
		return '-i'

def load_file(filename):
	f = open(filename,"r")
	i = 0
	j = 0
	for line in f:
		if i!=0:
			if i%2==0:
				a = []
				for sat in range(0,j):
					for x in line:
						if x != '\n':
							a.append(x)
				strings.append(a)
			else:
				l,js = line.split()
				j = int(js) 
		i += 1
def save_file(filename):
	f = open(filename,"w")
	i = 1
	for a in answers:
		f.write("Case #" + str(i)+ ": "+a+"\n")
		i += 1


def is_possible(s):
	#ks/////////
	ks = []
	sk = s[:]
	r = range(1,len(s))
	r.reverse()
	for i in r:
		if sk[i] == 'k':
			ks.append(i)
		a = xquad(sk[i-1],sk[i])
		sk.pop()
		sk.pop()
		sk.append(a)
	#is/////////
	js = []
	sk = s[:]
	sk.reverse()
	r = range(1,len(s))
	r.reverse()
	for i in r:
		if sk[i] == 'i':
			js.append(len(s)-i-1)
		a = xquad(sk[i],sk[i-1])
		sk.pop()
		sk.pop()
		sk.append(a)
	'''	q = "ks: "
	for x in ks:
		q += str(x) + " "
	print q
	q = "is: "
	for x in js:
		q += str(x) + " "
	print q'''
	for i in js:
		aux = []
		aux.append('1')
		index = -1
		for j in range(0,len(ks)):
			if i+1 < ks[j]:
				if index == -1:
					index = i + 1
				else:
					index = ks[j-1]
				aux += s[index:ks[j]]
				a = evaluate(aux)
				if a == 'j':
					return True
				aux = []
				aux.append(a)



	return False 

	

def evaluate(s):
	sk = s[:]
	r = range(1,len(s))
	r.reverse()
	for i in r:
		a = xquad(sk[i-1],sk[i])
		sk.pop()
		sk.pop()
		sk.append(a)
	return sk[0]


load_file("C-small-attempt3.in")
i = 1
for x in strings:
	print i
	i+=1
	'''	fo  = ""
	for jas in x:
		fo += jas
	print fo'''
	if is_possible(x):
		answers.append("YES")
		print "YES"
	else:
		answers.append("NO")
		print "NO"
save_file("out.txt")











