def isTidy(n):
	
	temp = n
	previous = 9
	while (temp):
		digit = temp % 10
		temp //= 10
		if (digit > previous):
			return False
		previous = digit
	return True

cases = int(input())

for case in range(cases):

	N = int(input())

	for number in range(N, 0, -1):
		if (isTidy(number)):
			print ("Case #", case+1, ": ", number, sep="")
			break
