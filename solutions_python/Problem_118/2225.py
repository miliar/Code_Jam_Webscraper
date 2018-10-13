import sys
from math import sqrt

def palindrome(n):
	return str(n)[::-1]

def is_Square(n):
    return n.is_integer()

def main():
	inFile = open('C-small-attempt0.in.in', 'r')
	outFile = open('out.txt', 'w')

	T = int(inFile.readline().strip())

	for i in range(T):
		A, B = inFile.readline().split()
		ans = 0
		for j in range(int(A), int(B)+1):
			n = sqrt(j)
			if (is_Square(n) and str(j) == palindrome(j)):
				s = int(n)
				if str(s) == palindrome(s):
					ans = ans + 1

		outFile.write("Case #%d: %s\n" % (i+1, ans))

	inFile.close()
	outFile.close()

if __name__ == '__main__':
	main()