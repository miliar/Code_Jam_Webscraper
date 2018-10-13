f=open('in','r')
w=open('out','w')
case=1
f.readline()

for line in f.readlines():
	line=line.split(' ')
	N=int(line[0])
	S=int(line[1])
	p=int(line[2])
	print ('Case '+str(case)+' p='+str(p))
	reg=0
	sup=0
	for i in range(3,N+3):
		s=int(line[i])
		q=s//3
		r=s%3
		tr=reg
		ts=sup
		if r==0:
			if q>=p:
				reg+=1
			elif q+1>=p:
				sup+=1
		elif r==1:
			if q+1>=p:
				reg+=1
		else:
			if q+1>=p:
				reg+=1
			elif q+2>=p:
				sup+=1
		if s<2 or s>28:
			if r==0 and q+1>=p and q<p:
				sup-=1
			elif r==2 and q+2>=p and q+1<p:
				sup-=1
		print (str(s)+': '+str(reg-tr)+' : '+str(sup-ts))

	w.write('Case #'+str(case)+': '+str(reg+min(S,sup))+'\n')
	case+=1

f.close()
w.close()
