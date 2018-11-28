import sys
import math

def is_square(n):
	return math.sqrt(n).is_integer()

def is_palindrome(int_in_question) :
	#print int_in_question
	as_list_of_chars = list( str( int_in_question))
	reversed_list_of_chars = list( as_list_of_chars)
	reversed_list_of_chars.reverse()
	return as_list_of_chars == reversed_list_of_chars

def count_palindrome_squares(low, up) :
	cnt = 0
	#print low, up
	for i in range(low, up+1):
		if is_square(i) == False:
			continue
		if is_palindrome(i):
			temp = int(math.sqrt(i))
			if is_palindrome(temp):
				cnt += 1
	return cnt

if __name__ == "__main__":
	N = int(sys.stdin.readline())
	i = 1
	while i <= N:
		low, up = sys.stdin.readline().split()
		cnt = count_palindrome_squares(int(low), int(up))
		print "Case #%d: %d" % (i, cnt)
		i += 1
