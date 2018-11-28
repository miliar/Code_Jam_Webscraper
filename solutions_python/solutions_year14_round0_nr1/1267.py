t=int(input())
counter=1
while(counter<=t):
	r=int(input())
	i=1
	
	string=[]

	while(i<=4):
		if(i==r):
			string=map(int,raw_input().split(" "))
		else:
			x=raw_input()
		i+=1
	r1=int(input())
	i=1
	pring=[]
	while(i<=4):
		if(i==r1):
			pring=map(int,raw_input().split(" "))
		else:
			x=raw_input()
		i+=1
	count=0
	number=0
	for x in string:
		for y in pring:
			if(x==y):
				count+=1
				number =x
	if(count==1):
		s="Case #"+str(counter)+": "+str(number)
		print s
	elif(count==0):
		s="Case #"+str(counter)+": Volunteer cheated!"
		print s
	else:
		s="Case #"+str(counter)+": Bad magician!"
		print s
	counter+=1
