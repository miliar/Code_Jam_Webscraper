
R=[]
G="BigCaseA.txt"

with open(r'A-large.in','rt') as arch:
	for line in arch:
		R.append([str(i) for i in line[0:-1].split()])

t=int(R.pop(0)[0])

filee=open(G,'w')

for j in range(t):
    Z=R[j]
    inv=0
    shy=int(Z[1][0])
    for i in range(1,int(Z[0])+1):
        p=int(Z[1][i])
        if shy>=i:
            shy+=p
        else:
            while shy<i:
                inv+=1
                shy+=1
            shy+=p
    filee.write('Case #%i: %i' %(j+1,inv))
    filee.write('\n')
