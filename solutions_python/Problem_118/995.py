import math
def findNumbers(a,b):
	ans=0
	start=int(math.ceil(math.sqrt(a)))
	i=start
	while True:
		iSq=pow(i,2)
		if iSq>b:
			break
		if i==int(str(i)[::-1]) and iSq==int(str(iSq)[::-1]):
			ans+=1
		i+=1
	return ans
lines=open('C-small-attempt0.in','r').readlines()[1:]
for i in range(len(lines)):
	lines[i]=lines[i].replace('\n','')
out=open('output.txt','w')
for i in range(len(lines)):
	nums=lines[i].split()
	a,b=int(nums[0]),int(nums[1])
	out.write(('Case #{0}: '+str(findNumbers(a,b))+'\n').format(i+1))