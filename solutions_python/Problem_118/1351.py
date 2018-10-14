'''
Created on 13/04/2013

@author: shb
'''
import sys

def is_palindrome(num):
	for n1, n2 in zip(num, num[::-1]):
		if n1 != n2:
			return False
	return True

if __name__ == '__main__':
	# brute force method
	n = int(sys.stdin.readline())
	for i in range(n):
		total = 0
		A, B = map(int, sys.stdin.readline().split())
		#print a, b
		a = int(A**.5)
		b=int(B**.5) + 1
		#print a, b
		
		for x in range(a, b+1):
			if is_palindrome(str(x)):
				if is_palindrome(str(x*x)):
					if A <= x * x <= B:
						total += 1
		
		print 'Case #{}: {}'.format(i+1, total)
		