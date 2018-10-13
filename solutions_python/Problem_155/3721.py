
def calculate(maxi,shy):
	ppl=0
	if shy[0]==0 : 
		ppl=1
		shy[0]=1
	cnt=shy[0]
	for i in range(1,maxi+1):
		
		if i<=cnt:
			cnt+=shy[i]
			
		else:
			ppl+=i-cnt
			cnt+=i-cnt
			cnt+=shy[i]
	return ppl



f=open("output.txt",'w')
ip=open('A-small-attempt15.in','r')
t=int(ip.readline())

for i in range(t):
	a=ip.readline()
	shy=[]
	ppl=0
	b=list(a)
	maxi=int(b[0])

	for j in b[2:maxi+3]:
		shy.append(int(j))
#	print(maxi,shy)
	ppl=calculate(maxi,shy)
	if i<t-1:
		a='Case #'+str(i+1)+': '+str(ppl)+'\n'
	else:
		a='Case #'+str(i+1)+': '+str(ppl)
#	print(a)
#	input()
	f.writelines(a)
ip.close()
f.close()