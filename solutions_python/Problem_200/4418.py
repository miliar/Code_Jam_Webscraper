testcase = input("")
#print type(testcase)
with open("in.txt", "r") as xt:
	topwrds_list = xt.read().split("\n")
   # testcase=topwrds_list[0]
for l in range(testcase):
	#num = input("")
	num = topwrds_list[l+1]
	number = num
	
	k = int(num)-1
	number1=int(num)+1
	num=str(num)
	p="0"
	q="0"
	
	#print type(number)
	#while(flag!="0"):
	for i in range(1,len(num)-1):
		if(num[i]=="0"):
			number1=num
			#print num
			num=int(num[0])-1

			num=str(num)
			if(num=="0"):
				num = ""
			for x in range(1,len(number1)):

				num=num+"9"
				
    
	while(num!=number1):
	 	num = str(num)
	 	if(len(num)>1):
	 		if(int(num)%10==0 and int(num)%100==0):
				num=int(num)-1
				break
	  		for i in range(len(num)-1):
			#print i
				number1=num
				#print type(num)
				num=str(num)
				if((int(num[i+1])-int(num[i]))<0):
					num = int(num)
					num=num-1
					
		else:
	 		number1=num

	print "Case #"+str(l+1)+": "+str(num)