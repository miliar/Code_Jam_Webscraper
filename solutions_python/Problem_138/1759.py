F = open('D-large.in').read()

def ken(cn, ks):
	for i,k in enumerate(ks):
		if(float(k) > float(cn)):
			return (i,k,ks)
	return (0,ks[0],ks)

def kend(cn, ks):
	for i,k in enumerate(ks):
		if(float(k) > float(cn)):
			return (i,k,ks)
	return (len(ks)-1,max(ks),ks)

def war(ws, ks, ns): #score with War rules
	for n in reversed(ns):
		ki,ck,ks = ken(n,ks)
		
		ks.pop(ki)
		ns.remove(n)
		if(float(n) > float(ck)):
			ws += 1
	return ws

def naomi(ns,ks):
	n = min(ns)
	ks.sort()
	ks = ks[::-1]

	if(max(ns) > max(ks)):
		return (max(ns),float(max(ns)),ns)

	if(ks[0] < n):
		return (n,float(n),ns);
	elif(len(ks)>1):
		return (n,(float(ks[0])-float(ks[1]))/2+float(ks[1]),ns)
	else:
		return (n,float(ks[0])-0.00001,ns)

def dwar(ds, ks, ns, N): # score with Deceitful War rules
	#rks = ks[::-1]
	rks = ks
	for i in range(0,int(N)):
		ni,cn,ns = naomi(ns,ks)
		ki,ck,rks = kend(cn,rks)
		'''print ns
		print ni
		print cn
		print rks
		print ck'''
		rks.pop(ki)
		ns.remove(ni)
		if(float(cn) > float(ck)):
			ds += 1
			#print ds
	return ds

f = F.split('\n')
T = f[0]

for t in range(0,int(T)):
	N = f[(t*3)+1]
	ns = n = f[(t*3)+2].split() # naomi's blocks
	ks = k = f[(t*3)+3].split() # ken's blocks
	
	ns2 = n = f[(t*3)+2].split() # naomi's blocks
	ks2 = k = f[(t*3)+3].split() # ken's blocks

	np = 0
	kp = 0

	ns.sort()
	ks.sort()

	ns2.sort()
	ks2.sort()
	ws = 0
	ds = 0
	
	#dw = 0
	w = war(ws,ks,ns)
	dw = dwar(ds,ks2,ns2,N)

	print "Case #%d: %d %d" % (t+1, dw, w)
	