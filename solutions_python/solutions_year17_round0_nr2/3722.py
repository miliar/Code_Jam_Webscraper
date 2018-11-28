def istidy(number):
	leftBound=0
	for i in range(len(number)):
		 if(number[i]==0):
		 	leftBound+=1
		 else:
		 	break
	for i in range(len(number)-2,leftBound-1,-1):
		if number[i]>number[i+1]:
			return i
	return -1
def solve(number):
	flag=istidy(number)
	while flag!=-1:
		number[flag]-=1
		for i in range(flag+1,len(number)):
			number[i]=9
		flag=istidy(number)
def createNumber(num):
	res=[]
	while num>0:
		res.append(num%10)
		num=num/10
	return list(reversed(res))
def createInt(number):
	res=0
	multiply=1
	for i in range(len(number)-1,-1,-1):
		res+=multiply*number[i]
		multiply*=10
	return res
tasklist=[]
lines = [line.rstrip('\n') for line in open('q2.inp')]
taskcount=int(lines.pop(0));
for i in range(taskcount):
	number=createNumber(int(lines.pop(0)))
	res=solve(number)
	print ("Case #"+str(i+1)+":"),createInt(number)		
	
