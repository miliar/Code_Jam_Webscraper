f=open("A-large.in")
def cal(s,k):
	if s.count("-")==0:return 0
	else:
		if k==1:return s.count("-")
		else:
			l,t,r=list(s),list(s),0
			while True:
				j=0
				for x in xrange(len(l)-k+1):
					if l[x]=="-":
						r,j=r+1,1
						for y in xrange(k):
							l[x+y]="-" if l[x+y]=="+" else "+"
				if l.count("-")==0:return r
				elif l==t or j==1:return "IMPOSSIBLE"
for _ in xrange(int(f.readline().strip())):
	s,k=f.readline().strip().split()
	print "Case #%d: %s"%(_+1,cal(s,int(k)))