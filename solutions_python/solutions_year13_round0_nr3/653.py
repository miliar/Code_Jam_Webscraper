
def isPalindrome(x):
	return x == x[::-1]

palindromes = [item for item in range(1,10**7 + 10) if isPalindrome(str(item))]

squarePalin = [item*item for item in palindromes if isPalindrome(str(item*item))]

filename = 'C-large-1.in'

f = open(filename,'r')

n = int(f.readline())
for i in range(0,n):
	line = f.readline()
	a = int(line.split(' ')[0])
	b = int(line.split(' ')[1])

	tot = len([item for item in squarePalin if item >= a and item <= b])

	print 'Case #' + str(i+1) + ': ' + str(tot)
