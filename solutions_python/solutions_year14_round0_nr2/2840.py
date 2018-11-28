
def count(c,f,x):
	n=2
	t=0
	while (x+0.0)/n >((c+0.0)/n + (x/(n+f+0.0))) :
		t+=(c+0.0)/n
		n+=f
	t=t+((x+0.0)/n)
	return t

if __name__=='__main__':
	fl = tuple(open('B-large.in', 'r'))
	outf=open('B-large.out','w')
	cas=int(fl[0])
	outs=''
	for i in range(1,cas+1):
		c,f,x=fl[i].split()
		r=count(float(c),float(f),float(x))
		outs+='Case #'+str(i)+': '+str(round(r,7))+'\n'
	outf.write(outs.strip())
	