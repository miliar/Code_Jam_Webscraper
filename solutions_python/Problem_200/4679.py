for i in range(int(input())):
	for num in range(int(input()),0,-1):
		tmp=True
		#print(num)
		for digit in range(1,len(str(num))):
			#print(str(num)[digit],str(num)[digit-1],digit)
			if str(num)[digit]<str(num)[digit-1]:
				tmp=False
				break
		if tmp:
			print("Case #"+str(i+1)+": "+str(num))
			break