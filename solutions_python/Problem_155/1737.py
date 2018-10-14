#input
f=open('A-large.in','r')
inp=[]
for line in f:
	inp.append(line)
f.close()
g=open('A.out','w')
x=int(inp[0])

#variables

#main
for i in range(x):
	s,k=map(str,inp[i+1].split(' '))
	s=int(s)
	t=[int(k[0]),0] #sum, added
	for j in range(1,s+1):
		if sum(t)<j:
			t[1]+=j-sum(t)
		t[0]+=int(k[j])
	g.write('Case #'+str(i+1)+': '+str(t[1])+'\n')
			
#output
g.close()
