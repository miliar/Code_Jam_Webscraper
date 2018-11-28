t2=int(input())
strngs2=[]
flip2=[]
z2=t2
while t2>0:
	li2=input().strip().split(' ')
	strngs2.append(li2[0])
	flip2.append(int(li2[1]))
	t2-=1
for i2 in range(z2):
	count2=0
	li2=list(strngs2[i2])
	
	while '-' in li2:
		j2=''.join(li2).rindex('-')
		flp2=flip2[i2]
		if j2-(flp2-1)>=0:
			for k2 in range(j2,j2-flp2,-1):
				if li2[k2]=='+':
					li2[k2]='-'
				else:
					li2[k2]='+'
			count2+=1
		else:
		
			count2=-2
			break	
		#print(li[i])
	if count2==-2:
		print("Case #"+str(i2+1)+": "+"IMPOSSIBLE")
	else:
		print("Case #"+str(i2+1)+": "+str(count2))


			
		
