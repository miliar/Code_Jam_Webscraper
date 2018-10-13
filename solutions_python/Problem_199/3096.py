t=int(input())
a1=[]
a2=[]
o=t
while t>0:
	d=input().split(' ')
	a1.append(d[0])
	a2.append(int(d[1]))
	t-=1
for i in range(o):
	z=0
	chk=list(a1[i])
	
	while '-' in chk:
		index=''.join(chk).rfind('-')
		#print(li,j)
		flips=a2[i]
		if index-(flips-1)>=0:
			for j in range(index,index-flips,-1):
				if chk[j]=='+':
					chk[j]='-'
				else:
					chk[j]='+'
			z+=1
		else:
			z=-2
			break	
		#print(li[i])
	if z==-2:
		print("Case #"+str(i+1)+": "+"IMPOSSIBLE")
	else:
		print("Case #"+str(i+1)+": "+str(z))


			
		
