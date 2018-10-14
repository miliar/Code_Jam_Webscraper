t=int(input())
strngs=[]
flip=[]
z=t
while t>0:
	li=input().strip().split(' ')
	strngs.append(li[0])
	flip.append(int(li[1]))
	t-=1
for i in range(z):
	count=0
	li=list(strngs[i])
	
	while '-' in li:
		j=''.join(li).rindex('-')
		#print(li,j)
		flp=flip[i]
		if j-(flp-1)>=0:
			for k in range(j,j-flp,-1):
				if li[k]=='+':
					li[k]='-'
				else:
					li[k]='+'
			count+=1
		else:
		
			count=-2
			break	
		#print(li[i])
	if count==-2:
		print("Case #"+str(i+1)+": "+"IMPOSSIBLE")
	else:
		print("Case #"+str(i+1)+": "+str(count))


			
		
