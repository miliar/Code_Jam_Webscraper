cases = int(input())
i=0
while i < cases :
	number = int(input())
	xnumber = number
	while(xnumber >0):
		if (sorted(list(str(xnumber))) == list(str(xnumber))):
			print("Case #"+ str(i+1)+": "+str(xnumber))
			break
		else:
			xnumber-=1
	i+=1