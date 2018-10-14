def isNumberPalindrome(num):
	digits = []
	while (num > 0) :
		digits.append(num % 10)
		num /= 10
	fl = len(digits)
	l = len(digits) / 2
	isPalindrome = True
	for i in range(l):
		if digits[i] != digits[fl - i - 1]:
			isPalindrome = False
	return isPalindrome

table = []
i = 1
while (i <= 1000) :
	if isNumberPalindrome(i) and isNumberPalindrome(i**2):
		table.append(i ** 2)
	i += 1;

T = int(raw_input())

for case in range(T):
	[A, B] = [int(c) for c in raw_input().split(' ')]
	ans = len([g for g in table if g >= A and g <= B])
	print "Case #" + str(case + 1) + ":", ans