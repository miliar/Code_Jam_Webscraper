
f=open("A-large.in","r")
g=open("OUTPUT.txt","w+")
T=int(f.readline())
for i in range(T):
	[k,s]=f.readline().split()
	k=int(k)
	invite=0
	running=0
	level=0
	for token in s:
		invite+=max(level-running,0)
		running+=max(level-running,0)
		running+=int(token)
		level+=1
	
	g.write("Case #{}: {}\n".format(i+1,invite))

f.close()
g.close()
