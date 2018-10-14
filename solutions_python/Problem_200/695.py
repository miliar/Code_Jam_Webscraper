# https://code.google.com/codejam/contest/3264486/dashboard#s=p1
def is_tidy(num):
	return str(num) == ''.join(sorted(str(num)))

def brute_solve(n):
	"""Brute-force. O(n)."""
	for potential in range(n, 1, -1):
		if is_tidy(potential):
			return potential
	return n if is_tidy(n) else -1

def smart_solve(n):
	"""Scan digits right-to-left. O(log n)."""
	digits = [int(d) for d in str(n)]
	# Scan digits from right-to-left, adjusting if they ever decrease.
	for i in range(len(digits) - 2, -1, -1):
		if digits[i] > digits[i+1]:
			# Decrement this digit and set all subsequent digits to 9.
			digits[i] -= 1
			for j in range(i+1, len(digits)):
				digits[j] = 9
	return int(''.join(str(d) for d in digits))

def main():
	cases = int(input())  # read a line with a single integer
	for case_num in range(1, cases + 1):
	  n = int(input())
	  print('Case #{}: {}'.format(case_num, smart_solve(n)))

def test():
	"""Compare brute-force and smart-solve for first 10000 integers."""
	for i in range(1, 10001):
		assert brute_solve(i) == smart_solve(i)


if __name__ == '__main__':
	main()