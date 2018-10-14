if __name__=='__main__':
	fl = list(open('A-small-attempt0.in', 'r'))
	outf=open('A-small-attempt0.out','w')
	cas=int(fl[0])
	outs=''
	for i in range(0,cas):
		o=i*10
		r1=int(fl[1+o])
		r2=int(fl[6+o])
		a=(set(fl[1+r1+o].split()))
		b=(set(fl[6+r2+o].split()))
		r=a.intersection(b)
		if len(r)==1:
			outs+='Case #'+str(i+1)+': '+str(list(r)[0])+'\n'
		elif len(r)==0:
			outs+='Case #'+str(i+1)+': Volunteer cheated!\n'
		elif len(r)>1:
			outs+='Case #'+str(i+1)+': Bad magician!\n'
	outf.write(outs.strip())