t = int(input())
for i in range(1, t + 1):
	n = int(input())
	
	while 1:
		valid = True
		number = list(str(n))
		#print (n)
		for j in range(0, len(number) - 1):
			if int(number[j + 1]) < int(number[j]):
				valid = False
				for k in range(j + 1, len(number)):
					number[k] = '9'
				number[j] = str(int(number[j]) - 1)
				n = int("".join(number))
				break
		if valid:
			print ("Case #{}: {}".format(i, n))
			break

'''
t = int(input())
for i in range(1, t + 1):
	n = int(input())
	
	while 1:
		valid = True
		number = str(n)
		for i in range(len(number) - 1, 0, -1):
			if int(number[i]) < int(number[i - 1]):
				valid = False
				if int(number[i]) == 0:
					n -= 1
				else:
					digit_difference = int(number[i - 1]) - int(number[i])
					factor = '1' + (len(number) - i)*'0'
					n -= digit_difference * int(factor)
				break
		if valid:
			print ("Case #{}: {}".format(i, number))
			break
'''


#test = 85498
#print (str(test)[0])
#print (len(str(test)))
'''
t = int(input())
for i in range(1, t + 1):
	n = int(input())
	for number in range (n, 0, -1):
		print (number)
		valid = True
		prev_digit = str(number)[0]
		for digit in str(number):
			if int(prev_digit) > int(digit):
				valid = False
				break
			prev_digit = digit
		if valid:
			print ("Case #{}: {}".format(i, number))
			break
'''