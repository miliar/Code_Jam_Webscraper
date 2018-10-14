f= open('input.in','r')
op = open('output.in','w')

t=int(f.readline())
for i in range(t):
	smax,slist = f.readline().split()
	smax = int(smax)
	slist = map(int,list(slist))
	minf = 0 
	ccount = slist[0]
	for j,elem in enumerate(slist):
		if j>0:
			if elem>0:
				if j>ccount:
					minf += j-ccount
					ccount = j
			ccount += elem



	op.write('Case #'+str(i+1)+': '+str(minf)+'\n')

f.close()
op.close()
