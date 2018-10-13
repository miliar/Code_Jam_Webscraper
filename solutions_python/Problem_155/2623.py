def calc (Smax,st,out=0,person=0):
	person+=int(st[0])
	for i in range(1,int(Smax)+1):
			while i>person:
				out+=1
				person+=1
			person+=int(st[i])
	return out

times=input()
shy=[]
for i in range(times):
	j=raw_input()
	Smax=j.split()[0]
	st=j.split()[1]
	out=calc(Smax,st)
	shy.append(out)
for i in range(times):
	print "Case #"+str(i+1)+":",shy[i]
