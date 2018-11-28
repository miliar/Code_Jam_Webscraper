def newcake(i,j):
	
	global cake
	global seen
	if cake[i][j] == '?':
		return
	
	val = cake[i][j]
	
	seen[(i,j)] = 1
	stackrow = []
	testlen = False
	icurr = i
	jcurr = j
	jbeg = j
	jend = j+1
	
	if jcurr+1<len(cake[0]):
		while (cake[icurr][jcurr+1]=='?'):
			stackrow.append((icurr,jcurr+1))
			seen[(icurr,jcurr+1)] = 1
			jcurr+=1
			if jcurr+1 == len(cake[0]):
				break
		if len(stackrow)>0:
			testlen = True
			for k in range(j,jcurr+1):
				cake[icurr][k] = val
			jend = jcurr+1
		
	icurrn = i
	jcurrn = j
	stackrow=[]
	if jcurrn - 1 >= 0:
		while (cake[icurrn][jcurrn-1]=='?'):
			stackrow.append((icurrn,jcurrn-1))
			seen[(icurrn,jcurrn-1)] = 1
			jcurrn-=1
			if jcurrn - 1<0:
				break
		
		if len(stackrow)>0:
			testlen = True
			for k in range(jcurrn,j+1):
				cake[i][k] = val
			jbeg = jcurrn
	
	test = 0
	icurrup = i
	if icurr>0:
		while(1):
			for k in range(jbeg,jend):
				if cake[icurr-1][k]!='?':
					test = 1
			if test == 1:
				break
			for k in range(jbeg,jend):
				cake[icurr-1][k] = val
				seen[(icurr-1,k)] = 1
			icurr-=1
			if icurr<=0:
				break
	
	test = 0
	if icurrup + 1 < len(cake):
		while(1):
			for k in range(jbeg,jend):
				if cake[icurrup+1][k]!='?':
					test = 1
			if test == 1:
				break
			for k in range(jbeg,jend):
				cake[icurrup+1][k] = val
				seen[(icurrup+1,k)] = 1
			icurrup+=1
			if icurrup + 1 == len(cake):
				break
		
	



fout = open('/Users/gorankovacevic/Desktop/D&A of Algos/Google/Code Jam Practice/Round 1A First/FirstBigOut.txt', 'w')

T = int(raw_input().strip())
case = 1

for i in range(T):
	R, C = [int(s) for s in raw_input().split(" ")]
	
	cake = []
	for i in range(R):
		line = raw_input()
		cake.append(line)
		
	cakenew = []
	cakenewrow = []
	for i in range(R):
		for j in range(C):
			cakenewrow.append(cake[i][j])
		cakenew.append(cakenewrow)
		cakenewrow = []
		
	cake = cakenew
	
	seen = {}
	for i in range(R):
		for j in range(C):
			if (i,j) not in seen:
				newcake(i,j)
	
	line1 = "Case #" + str(case) + ":" + "\n" 
	#print line1
	fout.write(line1)
	cakeout = []
	for i in range(R):
		cakeout.append('')
		for j in range(C):
			cakeout[i]+=cake[i][j]
	for i in range(R):	
		#print cakeout[i]
		fout.write(cakeout[i] + "\n")
	case += 1
		

			
	
		