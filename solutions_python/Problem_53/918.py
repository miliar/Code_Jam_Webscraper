import sys
state=[]
def toggle():
	global state
	n=1
	new_state=[]
	for i in state:
		new_state.append(i)
	if new_state[0]==0:
		new_state[0]=1
	else:
		new_state[0]=0
	while n<N:
		if state[n-1]==1:
			if new_state[n]==0:
				new_state[n]=1
			else: 
				new_state[n]=0
			n=n+1
		else:
			break
	state=new_state

f=open("A-small-attempt1.in","r")
T=int(f.readline())
i=0
while i<T:
	line=f.readline()
	NK=line.split()
	N=int(NK[0])
	K=int(NK[1])
	
	n=N	
	state=[]
	while n>0:
		state.append(0)
		n=n-1
	n=0
	while n<K:
		toggle()
		n=n+1
	sys.stdout.write("Case #")
	sys.stdout.write(str(i+1))
	sys.stdout.write(":")
	n=1
	for j in state:
		if j!=1:
			n=0
			break
	if n==1:
		sys.stdout.write(" ON\n")
	else: 
		sys.stdout.write(" OFF\n")
	i=i+1
