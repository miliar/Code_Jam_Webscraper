import re
import random
n = int(raw_input())
T = 1
while T <= n :
	count = 0
	S = raw_input()
	S = re.split(' ',S)
	num1 = int(S[0])
	num2 = int(S[1])
	#print num1,num2
	for i in range(num1,num2+1) :
		if str(i) != str(i)[::-1] :
			continue		
		a = 1
		flag = 0
		while(1) :
			if (a-1)**2 < i and a **2 > i :
				break
			if a**2 == i :
				if str(a) == str(a)[::-1] :
					flag = 1
				break
			elif a**2 > i:
				a = a-1
					
			else :
				a = a+1
		if flag == 1 :
			#print a,a**2
			count += 1

	print str("Case #"+str(T)+": "+str(count))
	T += 1
