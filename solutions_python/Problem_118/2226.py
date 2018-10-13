import math

def reverse(num):
	rev = 0
	
	tmp = num//10
	powTen = 1
	while tmp > 0:
		tmp //= 10
		powTen *= 10

	while num > 0:
		tmp = num % 10
		rev += (tmp * powTen)
		powTen //= 10
		num //= 10

	return rev

def is_palindrome(num):
	if reverse(num) == num:
		return True
	else:
		return False

if __name__ == '__main__':
	r = open('C-small-attempt0.in', 'r')
	w = open('out.txt', 'w')
	n = int(r.readline())

	for i in range(n):
		line = r.readline()
		line = line.rstrip()

		low, high = line.split(' ')
		low = int(low)
		high = int(high)
		count = 0
		for j in range(low, high+1):
			if is_palindrome(j):
				sq = int(math.sqrt(j))
				if sq**2 == j and is_palindrome(sq):
					count += 1

		w.write('Case #%d: %d\n' % (i+1, count))
