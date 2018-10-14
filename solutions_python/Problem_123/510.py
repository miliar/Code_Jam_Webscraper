def canWin(a,motes):
	for i in range(len(motes)):
		if a>motes[i]:
			a+=motes[i]
		else:
			return [a,i]
	return True
def operationsRequired(a,motes):
	if a==1:
		return len(motes)
	motes=sorted(motes)
	ops=0
	while True:
		t=canWin(a,motes)
		if t==True:
			return ops
		else:
			newMotes=motes.copy()
			index=t[1]
			inserts=0
			q=t[0]
			while q<=motes[t[1]]:
				newMotes.insert(index,q-1)
				index+=1
				q=q*2-1
				inserts+=1
			deletes=len(motes[t[1]:])
			if deletes<=inserts:
				return ops+deletes
			else:
				ops+=inserts
				motes=newMotes.copy()
lines=[i.replace('\n','') for i in open('A-small-attempt0.in','r').readlines()[1:]]
out=open('output.txt','w')
for i in range(0,len(lines),2):
	out.write(('Case #{0}: '+str(operationsRequired(int(lines[i].split()[0]),[int(j) for j in lines[i+1].split()]))+'\n').format(int(i/2)+1))