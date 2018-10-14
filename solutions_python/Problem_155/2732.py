input=open('A-large.in')
output=open('output-A.txt','w')
case_num=input.readline().strip()
case_num=int(case_num)
for t in range(case_num):
	smax, audi=input.readline().strip().split(' ')
	friends=0
	sum=0
	s=0
	for i in audi:
		i=int(i)
		if sum<s:
			friends=friends+s-sum
			sum=sum+i+s-sum
		else:
			sum=sum+i
		s=s+1
	output.write('Case #%d: %d\n' %(t+1,friends))

