def is_palindrom(number):
	number = str(number)
	return number == number[::-1]
	
def is_square(number):
     root = number**0.5
     if not number == int(root+0.5)**2:
     	return False
     return int(root)

testCases = int(raw_input())

for testCase in range(1, testCases+1):
	a,b = [int(x) for x in raw_input().split()]
	
	count = 0
	for num in range(a,b+1):
		if is_palindrom(num):
			root = is_square(num) 
			if  root != False:
				if is_palindrom(root):
					count += 1
	print "Case #" + str(testCase) + ":", count 
				
		
