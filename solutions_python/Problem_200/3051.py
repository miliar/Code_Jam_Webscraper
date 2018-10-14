def check_reverse(n):
	lis2 = sorted(lis)
	if lis2==lis:
		return 1
	else:
		return 0

def make(nums):
	num = int(''.join(map(str,nums)))
	return num

fp1 = open("input.in",'r')
t = int(fp1.readline())
fp = open("output.txt",'w')

for turn in range(t):
	n = int(fp1.readline())
	lis = []
	while n != 0:
		lis.insert(0,n%10)
		n/=10
	for item in range(len(lis),0,-1):
		if(check_reverse(lis)):
			break
		else:
			lis[item-1]=9
			lis[item-2] = lis[item-2]-1
	res = make(lis)
	if(turn==0):
		fp.write("Case #"+str(turn+1)+": "+str(res))
	else:
		fp.write("\nCase #"+str(turn+1)+": "+str(res))