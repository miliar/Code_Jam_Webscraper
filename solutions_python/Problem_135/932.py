def program(i):
	i+=1
	a=int(raw_input())
	for x in range(4):
		if x==a-1:
			data=map(int,raw_input().split())
		else:
			xxx=raw_input()

	a=int(raw_input())
	for x in range(4):
		if x==a-1:
			ans=map(int,raw_input().split())
		else:
			xxx=raw_input()
			
	temp=[]
	for x in ans:
		if x in data:
			temp.append(x)
	
	if not temp:
		print "Case #%d: Volunteer cheated!"%i
	elif len(temp)>1:
		print "Case #%d: Bad magician!"%i
	else:
		print "Case #%d: %d"%(i,temp[0])

n=int(raw_input())
for x in range(n):
	program(x)
