from sys import argv

def warO(n,nb,kb):
	if nb[0] > kb[n-1]:
		return n #sure victory
	elif nb[n-1] < kb[0]:
		return 0 #sure loss
	else:
		if nb[0] > kb[0]:
			if n > 1:
				i=0
				while nb[0] > kb[i]:
					i += 1
				kb.remove(kb[i])
				return 0 + warO(n-1,nb[1:],kb)
			else:
				return 1
		else:
			return 0 + warO(n-1,nb[1:],kb[1:])
				

def warD(n,nb,kb):
	if nb[0] > kb[n-1]:
		return n #sure victory
	elif nb[n-1] < kb[0]:
		return 0 #sure loss
	else:
		if nb[n-1] > kb[n-1]:
			return 1 + warD( n-1, nb[:n-1], kb[:n-1])
		else:
			return 0 + warD( n-1, nb[1:n], kb[:n-1])

def floatList( L ):
	m = L.split(" ")
	for i in range(0,len(m)):
		m[i] = float(m[i])
	m.sort()
	return m

def testCase(ln, args):
	#statements
	n = int(args[0]) #no. of blocks
	if n < 2:
		if float(args[1]) > float(args[2]):
			dw = w = 1
		else:
			dw = w = 0
	else:
		naomi = floatList(args[1])
		ken = floatList(args[2])
		dw = warD(n,naomi,ken)
		w = warO(n,naomi,ken)
	return "Case #%d: %d %d" % (ln,dw,w)

script, fname = argv

fil = open(fname)
fol = open("g-code-jam-2014-d",'w')

N = int(fil.readline())

for i in range(0,N):
	args=[]
	#parse the input
	for j in range(0,3):
		temp = fil.readline()
		args.append(temp[:-1])
	fol.write( testCase( i+1, args ) )
	if i < N-1:
		fol.write("\n")
