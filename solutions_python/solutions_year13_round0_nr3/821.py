import sys
import string
from math import *

def is_palindrome(n):
	return str(n)[::-1] == str(n)

def main():
	t = int(sys.stdin.readline())

	memo = []	
	for j in range (1, 10000000 + 1):
		if is_palindrome(j) and is_palindrome(j * j):
			memo.append(j * j)

	for i in range(t):
		inputs = map(int, sys.stdin.readline().split(' '));
		n = inputs[0];
		m = inputs[1];
		count = 0;
		
		for mm in memo:
			if mm <= m and mm >=n:
				count = count + 1
		print "Case #" + str(i + 1) + ": " + str(count)

if __name__ == "__main__":
	main()