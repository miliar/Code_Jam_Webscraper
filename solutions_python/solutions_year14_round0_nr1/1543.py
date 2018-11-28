from sys import argv

def intList( L ):
	m = L.split(" ")
	for i in range(0,len(m)):
		m[i] = int(m[i])
	return m

def testCase(ln, args):
	#statements
	r1 = int(args[0])
	l1 = intList(args[r1])
	print l1
	r2 = int(args[5])
	print r2
	l2 = intList(args[5+r2])
	print l2
	flag = 0
	Ans = -1
	for i in l1:
		for j in l2:
			if i == j:
				Ans = j
				flag+=1
	if flag > 1:
		Ans = "Bad magician!"
	elif flag == 0:
		Ans = "Volunteer cheated!"
	else:
		pass
	return "Case #%d: %s" % (ln,Ans)

script, fname = argv

fil = open(fname)
fol = open("g-code-jam-2014-a",'w')

N = int(fil.readline())

for i in range(0,N):
	args=[]
	#parse the input
	for j in range(0,10):
		temp = fil.readline()
		args.append(temp[:-1])
	print args
	fol.write( testCase( i+1, args ) )
	if i < N-1:
		fol.write("\n")
