def isTidy(number):
	string_number = str(number)
	x = 1
	for char in string_number:
		if int(char) >= x:
			x = int(char)
		else:
			return False
	return True

T = int(input())
for i in range(T): #All test cases are covered
	number = int(input())
	tidy = False
	while(not tidy):
		tidy = isTidy(number)
		number -= 1
	print("Case #{}: {}".format(str(i+1), str(number + 1)))
