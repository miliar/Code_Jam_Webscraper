for t in range(1,int(input())+1):
	r1=int(input())
	for i in range(1,4+1):
		if i==r1:
			row1=set(input().split())
		else:
			input()
	
	r2=int(input())
	for i in range(1,4+1):
		if i==r2:
			row2=set(input().split())
		else:
			input()

	com=row1&row2
	
	if(len(com)==1):
		ans=com.pop()
	elif(len(com)==0):
		ans="Volunteer cheated!"
	elif(len(com)>1):
		ans="Bad magician!"
	
	print("Case #{}: {}".format(t,ans))