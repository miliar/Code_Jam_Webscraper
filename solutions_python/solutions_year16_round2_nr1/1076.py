
def findtelnumber(number,S,curnum):
	if not S:
		return number
	numbers=["ZERO", "TWO", "FOUR", "SIX", "EIGHT","ONE","THREE","FIVE","SEVEN" ,"NINE" ]
	mapping=[0,2,4,6,8,1,3,5,7,9]
	lencurnum=len(numbers[curnum])
	#print(lencurnum)
	#innumber=False
	locations=[]
	for k in range(0,lencurnum):
		locations.append(S.find(numbers[curnum][k]))
	if -1 in locations:
		if curnum<9:
			return findtelnumber(number,S,curnum+1)
		else:
			return number
	else:
		SR=""
		for j in range(0,len(S)):
			if not j in locations:
				SR=SR+S[j]
		number.append(mapping[curnum])
		return findtelnumber(number,SR,curnum)
	return(0)
t = int(input()) 
for i in range(1, t + 1):
	S=str(input())
	number=list()
	n=findtelnumber(number,S,0)
	n.sort()
	num=""
	for k in range(0,len(number)):
		num=num+str(n[k])
	
	#print(num)
	print("Case #{}: {}".format(i,num))