def convert_to_number( a ):
	temp=a.strip();
	ans = map(float,temp.split(' '))
	return ans



fin=open("input.txt","r")
test_cases=[]
test_cases=fin.readlines()
no=int(test_cases[0][0:-1])
for i in range(1,no+1):
	l=convert_to_number(test_cases[i])
	c=l[0]
	f=l[1]
	x=l[2]
	cookies=[]
	
	answer=0.0
	target=x/float(2)
	farm=c/float(2)
	farm_points=[farm]
	if target <=farm:
		answer=target
		print 'Case #'+str(i)+': '+str(format(answer,'.7f'))
		continue
	counter = 1
	for j in range(0,1000000):
		
		cookies.append(x/float(2.0+counter*f))
		
		if sum(farm_points)+cookies[-1]<target:
			target = cookies[-1]+sum(farm_points)
		else:
			answer=target
			break
		farm_points.append(c/float(2.0+counter*f))
		counter=counter+1

	print 'Case #'+str(i)+': '+str(format(answer,'.7f'))