import math;
import gmpy;


def check_palindrome(i):
	if str(i) == str(i)[::-1]:
		return 1
	else:
		return 0


if __name__ == "__main__":
	t = input()
	for i in range(0, t):
		count = 0
		n, m = raw_input().split()
		n = long(n)
		m = long(m)
		minimum = gmpy.sqrt(n)
		minimum -= 1
		while True:
			if minimum*minimum < n:
				minimum += 1
			else:
				break

		#print minimum
		#print minimum*minimum

		maximum = gmpy.sqrt(m)
		maximum += 1
		while True:
			if maximum*maximum > m:
				maximum -= 1
			else:
				break

		#print maximum
		#print maximum*maximum

		while minimum <= maximum:
			if check_palindrome(minimum):
				if check_palindrome(minimum*minimum):
					#print minimum*minimum
					count += 1

			minimum += 1


		out = "Case #" + str(i+1) + ": " + str(count)
		print out