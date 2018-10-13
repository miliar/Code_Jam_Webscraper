def isPalindrome(string):
	palindrome = True
	for i in range(0, len(string) / 2 + 1):
		if(string[i] != string[len(string) - 1 - i]):
			return False
	return True

numbers = []
for i in range(0, 10 ** 7):
	string1 = str(i)
	string2 = str(i**2)
	if(isPalindrome(string1) and isPalindrome(string2)):
		numbers.append(int(string2))


inputfile = open("pal-input.txt", "r")
output = open("palsquares-output.txt", "w")
a = 0;
for line in inputfile:
	count = 0;
	if(a != 0):
		nums = [int(n) for n in line.split()]
		for x in numbers:
			if(x >= nums[0]):
				if(x <= nums[1]):
					count = count + 1
				else:
					break
		output.write("Case #" + str(a) + ": " + str(count) + '\n')
	a = a + 1
	



print numbers


