f=open('A-small-attempt0.in','r')
o=open('oas','w+')
t=int(f.readline())




def trep(x):
	wr=[x[i] for i in range(len(x)-1) if x[i+1]!= x[i]]
	wr.append(x[-1])
	return wr

def gdict(r,w0):
	i=0
	w=[c for c in w0]
	d=[]
	for c in r:
		s=0
		while len(w)>0 and w[0]==c:
			s+=1
			w.pop(0)
		d.append((c,s))
			
	return d


ti=1
while ti<=t :
	n=int(f.readline())
	w1=f.readline().strip()
	w2=f.readline().strip()
	if w1==w2:
		s="0"
	else:
		x1=trep(w1)
		x2=trep(w2)
		if( x1!=x2):
			s="Fegla Won"
		else:
			d1=gdict(x1,w1)
			d2=gdict(x1,w2)
			d=0
			for i in range(len(x2)):
				d+=abs(d2[i][1]-d1[i][1])
				# print d
			s=d
	ss= str("Case #")+str(ti)+str(": ")+ str(s)+str("\n")
	o.write(ss)


	ti+=1


def trep(x):
	wr=[x[i] for i in range(len(x)-1) if x[i+1]!= x[i]]
	wr.append(x[-1])
	return wr

def gdict(r,w0):
	i=0
	w=[c for c in w0]
	d=[]
	for c in r:
		s=0
		while len(w)>0 and w[0]==c:
			s+=1
			w.pop(0)
		d.append((c,s))
			
	return d
