def pancakes(sit,k):
	#[0,1,0,0,1,1,0,1]
	counter=0
	for n in xrange(len(sit)-k+1):
		if (sit[n]==False):
			counter+=1
			for i in xrange(k):
				sit[n+i]=not(sit[n+i])
	if (False in sit[-k:]):
		return "IMPOSSIBLE"
	return counter

f=open("C:\\Users\\Saar\\Desktop\\input.txt",'r')
f2=open("C:\\Users\\Saar\\Desktop\\output.txt",'w')
lines=f.readlines()[1:]
sit=""
k=""
lst=[]
for i,line in enumerate(lines):
	sit,k=line.split(' ')
	lst=list(sit)
	for cell in xrange(len(lst)):
		if lst[cell]=='-':
			lst[cell]=False
		else:
			lst[cell]=True
	f2.write("Case #"+str(i+1)+": "+str(pancakes(lst,int(k)))+"\n")

f.close()
f2.close()