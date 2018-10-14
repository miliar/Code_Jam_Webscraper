def check(num, p):
	if p==0:
		return 2
	if p==1:
		if num>0:
			return 2
		else:
			return 0
	if p>1:
		temp=(2*p)-4
		x=p+temp

	if num<x:
		return 0
	if num==x or num==(x+1):
		return 1
	return 2

finput = open("inputb.txt", "r")
foutput = open("outputb.txt", "w")

t=int(finput.readline())

for i in range(0,t):
	nums=finput.readline().split()
	n, s, p = int(nums[0]), int(nums[1]), int(nums[2])
	surprise, works = 0, 0
	
	for j in range(0,n):
		num=int(nums[j+3])
		z=check(num, p)
		if z==0:
			pass
		if z==1:
			surprise+=1
		if z==2:
			works+=1
	if surprise>=s:
		endsurprise=s
	else:
		endsurprise=surprise

	result=works+endsurprise
	foutput.write("Case #" + str(i+1) + ": " + str(result)+"\n")	

finput.close()
foutput.close()