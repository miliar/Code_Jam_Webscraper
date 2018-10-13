import math

def is_palindrome(s):
	return (s == s[::-1])


fin = open('C-small-attempt1.in', 'r')
fout = open('C-small-attempt1.out', 'w')
limit = fin.readline().strip('\r\n')

sample = {}
#limit = 1000
for t in range(int(limit)):
	a, b = map(int, fin.readline().strip('\r\n').split(' '))
	
	cnt = 0
	sqrt_a = int(math.sqrt(a))
	sqrt_b = int(math.sqrt(b))
	
	for i in range(sqrt_a, sqrt_b+1):
		check = i*i
		if check >= a and check <= b:
			if is_palindrome(str(i)) and is_palindrome(str(check)):
				cnt = cnt + 1

	fout.write("Case #%i: %i\n" %(t+1, cnt))

fout.close()
fin.close()
