def is_palindrome(n):
	if(n % 1 != 0):
		return False
	else:
		n = int(n)
		n = str(n)
	reverse = n[::-1]
	if reverse == n:
		return True
	else:
		return False



file = open("testq3.in", "r")
num_tests = file.readline().rstrip()
num_tests = int(num_tests)


for x in range(0, num_tests):
	input = file.readline().rstrip()
	limits = input.split()
	num_fair = 0

	for i in range(int(limits[0]), int(limits[1]) + 1):
		if(is_palindrome(i)):
			if(is_palindrome(i ** 0.5)):
				num_fair+= 1


	print "Case #" + repr(x + 1) + ": " + repr(num_fair)
