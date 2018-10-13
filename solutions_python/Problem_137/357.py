done = False
t = int(input())
r = c = m = 0
delta = [(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1),(0,1),(0,-1)]

def next_candidates(p,d,x,r,c):
	rslt = []
	for dl in delta:
		if x[0]+dl[0] >= 0 and x[0]+dl[0]<c and x[1]+dl[1] >=0 and x[1]+dl[1] < r:
			newp =(x[0]+dl[0],x[1]+dl[1])
			if newp not in p and newp not in d:
				rslt.append(newp)
	return rslt

reslt = []
rc = (0,0)
def f(p,d,x,r,c):
	global reslt
	global done
	global rc
	if not done:
		p.append(x)
		newcan = next_candidates(p,d,x,r,c)
		for i in newcan: d.append(i)
		if (len(d)+1 == r*c-m):
			done = True
			reslt = d + p
			rc = x
			return
		for i in newcan: f(p,d,i,r,c)
		for i in newcan: d.remove(i)
		p.remove(x)


for testcase in range(1, t+1):
	r,c,m = map(int, input().split())
	print("Case #" + str(testcase) + ":")
	for ci in range(c):
		for ri in range(r):
			f([],[],(ci,ri),r,c)
	if r*c-1 == m:
		done = True
		reslt = [(0,0)]
		rc = (0,0)
	if not done:
		print("Impossible")
	else:
		op = []
		for i in range(r):
			rw = []
			for j in range(c):
				rw.append("*")
			op.append(rw)
		for i in reslt:
			op[i[1]][i[0]] = "."
		op[rc[1]][rc[0]] = "c"
		for i in op:
			print ("".join(i))
				
	done = False
