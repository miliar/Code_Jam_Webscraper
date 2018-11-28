from math import floor, ceil, sqrt

f = open('fairsquare.in')
out = open('fairsquare.out', 'w')
cases = int(f.readline())

def isPalindrome(num):
	string = str(num)
	if string == string[::-1]:
		return True
	else:
		return False

for case in range(1, cases+1):
	input = f.readline().split()
	start = ceil(sqrt(int(input[0])))
	end = floor(sqrt(int(input[1])))

	counter = 0
	for i in range(start, end+1):
		if isPalindrome(i):
			if isPalindrome(i*i):
				counter += 1

	out.write("Case #{0}: {1}\n".format(case, counter))
