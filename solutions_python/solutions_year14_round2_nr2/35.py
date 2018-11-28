import sys

def takle(c,a,ba,b,bb):
	acc = 0
	if len(c)==0:
	
		return 1
	if c[-1]==0:
		#00
		if ba:
			if a[-1]==0:
			#a takes 0 only
				if bb:
					if b[-1]==1:
						acc+=takle(c[:-1],a[:-1],True,b[:-1],True)+takle(c[:-1],a[:-1],True,b[:-1],False)
					else:
						acc+=takle(c[:-1],a[:-1],True,b[:-1],True)
				else:
					acc+=takle(c[:-1],a[:-1],True,b[:-1],False)*2
			else:
				if bb:
					if b[-1]==1:
						acc+=takle(c[:-1],a[:-1],True,b[:-1],False)+takle(c[:-1],a[:-1],False,b[:-1],True)+takle(c[:-1],a[:-1],False,b[:-1],False)
					else:
						acc+=takle(c[:-1],a[:-1],True,b[:-1],True)+takle(c[:-1],a[:-1],False,b[:-1],True)
				else:
					acc+=takle(c[:-1],a[:-1],True,b[:-1],False)+takle(c[:-1],a[:-1],False,b[:-1],False)*2
		else:
			if bb:
				if b[-1]==1:
					acc+=takle(c[:-1],a[:-1],False,b[:-1],True)+takle(c[:-1],a[:-1],False,b[:-1],False)*2
				else:
					acc+=takle(c[:-1],a[:-1],False,b[:-1],True)*2
			else:
				acc+=takle(c[:-1],a[:-1],False,b[:-1],False)*3
	if c[-1]==1:
		if ba:
			if a[-1]==0:
			#a takes 0 only
				acc+=0
			else:
				if bb:
					if b[-1]==1:
						acc+=takle(c[:-1],a[:-1],True,b[:-1],True)
					else:
						acc+=0
				else:
					acc+=takle(c[:-1],a[:-1],True,b[:-1],False)
		else:
			if bb:
				if b[-1]==1:
					acc+=takle(c[:-1],a[:-1],False,b[:-1],True)
				else:
					acc+=0
			else:
				acc+=takle(c[:-1],a[:-1],False,b[:-1],False)
	if c[-1]==-1:	
		if ba:
			if a[-1]==0:
			#a takes 0 only
				if bb:
					if b[-1]==1:	
						acc+=takle(c[:-1],a[:-1],True,b[:-1],True)+takle(c[:-1],a[:-1],True,b[:-1],False)
					else:
						acc+=takle(c[:-1],a[:-1],True,b[:-1],True)
				else:
					acc+=takle(c[:-1],a[:-1],True,b[:-1],False)*2
			else:
				if bb:
					if b[-1]==1:
						acc+=takle(c[:-1],a[:-1],True,b[:-1],False)+takle(c[:-1],a[:-1],False,b[:-1],True)+takle(c[:-1],a[:-1],False,b[:-1],False)+takle(c[:-1],a[:-1],True,b[:-1],True)
					else:
						acc+=takle(c[:-1],a[:-1],True,b[:-1],True)+takle(c[:-1],a[:-1],False,b[:-1],True)
				else:
					acc+=takle(c[:-1],a[:-1],True,b[:-1],False)*2+takle(c[:-1],a[:-1],False,b[:-1],False)*2
		else:
			if bb:
				if b[-1]==1:
					acc+=takle(c[:-1],a[:-1],False,b[:-1],True)*2+takle(c[:-1],a[:-1],False,b[:-1],False)*2
				else:
					acc+=takle(c[:-1],a[:-1],False,b[:-1],True)*2
			else:
				acc+=takle(c[:-1],a[:-1],False,b[:-1],False)*4
	#raw_input()
	return acc
def bitand(a,b):
	tmpa = a
	alist = []
	while tmpa>0:
		alist.append(tmpa%2)
		tmpa = tmpa/2
	tmpb = b
	blist = []
	while tmpb>0:
		blist.append(tmpb%2)
		tmpb = tmpb/2
	clist = []
	while len(alist)<len(blist):
		alist.append(0)
	while len(blist)<len(alist):
		blist.append(0)
	for i in range(0,len(alist)):
		clist.append(alist[i] and blist[i])	

	c = 0
	for i in range(0,len(clist)):
		c = c*2+clist[len(clist)-1-i]
	return c

def solve(fin,fout):
	f = open(fin,'r')
	out = open(fout,'w')

	T = int(f.readline())
	for t in range(0,T):
		out.write("Case #%d: "%(t+1))	
		
		tokens = f.readline().split()
		A = int(tokens[0])
		B = int(tokens[1])
		C = int(tokens[2])
		acc = 0
		tmpc = C
		clist = []
		while tmpc>0:
			clist.append(tmpc%2)
			tmpc = tmpc/2
		
		alist = []
		A = A-1
		B=B-1
		tmpa=A
		while tmpa>0:
			alist.append(tmpa%2)
			tmpa = tmpa/2
		tmpb = B
		blist = []
		while tmpb>0:
			blist.append(tmpb%2)
			tmpb = tmpb/2
		maxlen = max(len(alist),len(blist),len(clist))
		while len(alist)<maxlen:
			alist.append(0)

		while len(blist)<maxlen:
			blist.append(0)

		while len(clist)<maxlen:
			clist.append(0)
		for i in range(0,len(clist)):
			tmpclist = clist[:]
			if clist[i]==1:
				tmpclist[i]=0
				for j in range(0,i):
					tmpclist[j]=-1
				acc = acc + takle(tmpclist,alist,True,blist,True)
		out.write("%d\n"%acc)
	f.close()
	out.close()
if __name__=="__main__":
	solve(sys.argv[1],sys.argv[2])
