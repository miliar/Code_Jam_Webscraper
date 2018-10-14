for _ in range(int(input())):
	number=input()
	length=len(number)
	myans,index='',length
	first_number=int(number[0])
	flag=0
	for i in range(length-1):
		if int(number[i])>int(number[i+1]):
			if length>2:
				while int(number[i-1])==int(number[i]):
					flag=1
					index=i-1
					i-=1
				if flag==0:
					index=i
			else:
				index=i
			break
	new_number=number[index:]	
	#print (new_number)
	if new_number=="":
		ans=number
	else:
		lengthn=len(new_number)
		myans+=str(int(new_number[0])-1)
		for k in range(lengthn-1):
			myans+='9'
	print ("Case #{}: {}".format(_+1,(number[:index]+myans).lstrip('0')))
	