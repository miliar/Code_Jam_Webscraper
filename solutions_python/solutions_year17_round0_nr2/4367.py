T = int(raw_input())

final = []

def check(n):
	
	number = n
	while(n > 0):
		if(n < 10):
			return number
		if(n%10 >= (n/10)%10):
			n /= 10
		else:
			max1 = 0
			length = len(str(number))
			stringNum = str(number)
			for i in range(length):
				if (int(stringNum[i]) >= max1):
					max1 = int(stringNum[i])
					pos = i
				else:
					stringNumber = stringNum[:pos] + str(max1-1) + '9' * (length-(pos+1))
					number = int(stringNumber)
					n = number


for i in range(T):

	n = int(raw_input())
	

	n = check(n)
		
	final.append(n)
	

for i in range(T):
	print "Case #%d: %d" %(i+1,final[i]) 

