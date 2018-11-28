def Yes():
	g.write("Case #")
	g.write(str(i+1))
	g.write(": YES\n")

def No():
	g.write("Case #")
	g.write(str(i+1))
	g.write(": NO\n")

def check(a,b,c,d,t,low,p1,p2):
	return (vert_check(p1,c,d,t,low) or hor_check(a,b,p2,t,low))

def vert_check(p,c,d,t,low):
	bol = True
	for temp in range(c,d):
		if t[p][temp]!=low:
			bol=False
			break
	return bol

def hor_check(a,b,p,t,low):
	bol = True
	for temp in range(a,b):
		if t[temp][p]!=low:
			bol=False
			break
	return bol

def check2(a,b,c,d,t,low,p1,p2):
	return (vert_check2(p1,c,d,t,low) or hor_check2(a,b,p2,t,low))

def vert_check2(p,c,d,t,low):
	bol = False
	for temp in range(c,d):
		if t[p][temp]==low:
			bol=True
			break
	return bol

def hor_check2(a,b,p,t,low):
	bol = False
	for temp in range(a,b):
		if t[temp][p]==low:
			bol=True
			break
	return bol

def findLocalMin(a,b,c,d,t):
	min = 101
	for x in range(a,b):
		for y in range(c,d):
			if t[x][y]<min:
				min = t[x][y]
	return min 

def verify(a,b,c,d,t):
	if a>=b or c>=d:
		return True
	m = findLocalMin(a,b,c,d,t)
	miau=True
	for x in range(a,b):
		print x , c
		if t[x][c]==m:
			if not check(a,b,c,d,t,m,x,c):
				miau=False
		if t[x][c]>m:
			print "here"
			if not check2(a,b,c,d,t,m,x,c):
				print "hey"
				miau=False		
		if t[x][d-1]==m:#-1		
			if not check(a,b,c,d,t,m,x,d-1):
				miau=False
		if t[x][d-1]>m:
			if not check2(a,b,c,d,t,m,x,d-1):
				miau=False
	if miau:
		for y in range(c,d):
			if t[a][y]==m:
				if not check(a,b,c,d,t,m,a,y):
					miau=False
			if t[b-1][y]==m:#-1
				if not check(a,b,c,d,t,m,b-1,y):
					miau=False
			if t[a][y]>m:
				if not check2(a,b,c,d,t,m,a,y):
					miau=False
			if t[b-1][y]>m:#-1
				if not check2(a,b,c,d,t,m,b-1,y):
					miau=False
	if miau:
		miau = verify(a+1,b-1,c+1,d-1,t)
	return miau

# open input and output files
f = open('input','r')
g = open('output','w')

# for i 0...(N-1)
for i in range(int(f.readline())):
	temp = f.readline().strip().split()
	n = int(temp[0])
	m = int(temp[1])
	pattern=[]	
	for j in range(n):
		line=[]
		temp = f.readline().strip().split()
		for k in range(m):
			line.append(int(temp[k]))
		pattern.append(line)
	min = findLocalMin(0,n,0,m,pattern)
	new_pat=[]
	new_pat.append([min]*(m+2))
	for j in range(n):
		temp = [min]
		temp+=pattern[j]
		temp.append(min)
		new_pat.append(temp)
	new_pat.append([min]*(m+2))
	print
	for j in range(n+2):
		for k in range(m+2):
			print new_pat[j][k],
		print
	print	

	flag = verify(0,n+2,0,m+2,new_pat)
	
	if flag:
		Yes()
	else:
		No()

f.close()
g.close()

