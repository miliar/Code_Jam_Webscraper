from decimal import *
a=raw_input()
arr1=[]
arr2=[]

for i1 in range(0,int(a)):
	b=raw_input()
	arr1.append(b)
# getcontext().prec=7	
# print arr1
for i in range(0,int(a)):
	time1=0
	time2=0
	cond=0
	pro=2
	ct=0
	tt=0
	temp=arr1[i].split(' ')
	# print temp
	temp[0]=float(temp[0])
	temp[1]=float(temp[1])
	temp[2]=float(temp[2])
	# print temp[2]/pro
	while(cond==0):
		# time taken if i buy a farm
		time1=temp[0]/pro
		# time taken if i complete my ultimate goal
		time2=temp[2]/pro
		#if  i buyed a farm then  total time to reach goal (tt=time to buy farm + time to reach goal with new production):
		pro1=pro + temp[1]
		tempt=time1+temp[2]/pro1
		if(time2 < tempt):
			cond=1
			tt=tt+time2
		else:
			pro=pro1
			tt=tt+time1
		



		# else:
		# print "tt=",tt
		# print "pro=",pro
		# raw_input()


	str1="Case #"+str(i+1)+":"
# print (tt)
	print str1,'{0:.7f}'.format(tt)