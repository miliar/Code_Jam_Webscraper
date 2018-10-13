def minimizer(n):
	a=map(int, n) 
	if(len(a)<2 or a[0]<1):
		return n
	asak = True
	while asak:
		asak=False
		for x in xrange(len(a)-1):
			if(a[x]>a[x+1]):
				for i in xrange(x+1,len(a)):
					a[i]=9
				a[x]-=1
				asak=True
				break
	if(a[0]<1):
		a=a[1:]
	k = int(''.join(map(str,a)))
	return k

	
f=open("C:\\Users\\Saar\\Desktop\\input.txt",'r')
f2=open("C:\\Users\\Saar\\Desktop\\output.txt",'w')
lines=f.readlines()[1:]
#last=lines[-1]
#lines=lines[:-1]
r=""
t=""
for i,line in enumerate(lines):
	line=line[:-1]
	f2.write("Case #"+str(i+1)+": "+str(minimizer(line))+"\n")
#f2.write("Case #"+str(i+2)+": "+str(minimizer(last))+"\n")
f.close()
f2.close()
#489

#22994
#834
#716