
fo = open("magicka.in") #B-small-attempt0.in")
#print fo.readlines()
T = int(fo.readline())
C = -1
D = -1

combos = {}
destros = set([])
for t in range(T):
	combos = {}
	destros = set([])
	strs = fo.readline().split()
	#print t	
	#print strs
	C = int(strs[0])
	for c in range (C):
		cs = strs[1+c]
		combos[cs[0:2]] = cs[2]
		combos[cs[0:2][::-1]] = cs[2]
		#print "Cs:", c, cs
	D = int(strs[1+C])
	for d in range (D):
		ds = strs[2+C+d]
		destros.add( ds[0:2]) 
		destros.add( ds[0:2][::-1])
		#print "Ds:", d, ds
	#print "destros =", destros
	#print "combos =", combos
	elementlist = strs[-1]
	cur = []
	for c in elementlist:
		cur.append(c)
		potcombo = "".join(cur[-2:])
		#print "cur is", cur, "potcombo is",potcombo
		if str(potcombo) in combos:
			del cur[-2:]	
			cur.append(combos[potcombo])
			#print "combined! by", potcombo
		for destro in destros:
			if destro[0] in cur and destro[1] in cur:
				cur = []
				#print "destroyed! by ", destro
	output = "Case #"+str(t+1)+": ["
	for char in cur:
		output+=str(char)+", "
	if len(cur)>0:
		output = output[0:-2]
	output+="]"
#+map(lambda x: str(x)+', ',cur)  )
	print output #"Case #", cur
			
	#print "\n"
	 
	
