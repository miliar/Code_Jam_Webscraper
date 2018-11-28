t = int(raw_input())

for i in range(1, t + 1):
	num = int(raw_input())
	tidy = False
	
	#while not tidy
	#for num, num-1, -1...
	#loop through string of number
	#if previous # > current or completed parse, stop loop
	num +=1
	while not tidy:
		num -=1
		prev = 0
		tidy = True
		for digit in str(num):
			if prev <= digit:
				prev = digit
			else:
				 tidy = False
				 break

	print ("Case # "+ str(i) + ": "+ str(num))


