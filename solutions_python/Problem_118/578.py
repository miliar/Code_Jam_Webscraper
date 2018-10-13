import sys
import math

def is_palindrome(number):
	
	written = str(number)
	if written[:(len(written))/2] == written[(len(written)+1)/2:][::-1]: return True
	return False

def next_palindrome(current, current_is_palindrome=False):

	written    = str(current)
	digits     = len(written)
	first_half = int(written[:(digits+1)/2])
	
	if current_is_palindrome:
		if written.replace('9','') == "": return current+2
		first_half += 1
		if len(str(first_half)) > len(str(first_half-1)): digits += 1
	
	if digits % 2 == 0:
		return int(str(first_half)+str(first_half)[::-1])
	else:
		return int(str(first_half)+str(first_half)[:-1:][::-1])

def palindrome_generator(start, end):

	palindrome = next_palindrome(start)
	while palindrome <= end:
		if palindrome >= start:	yield palindrome
		palindrome = next_palindrome(palindrome, True)

if __name__ == '__main__':
	
	input_ = sys.stdin.readlines()[1:]
	for test_case, line in enumerate(input_):
		A, B  = line.strip().split()
		start = int(math.ceil(math.sqrt(float(A))))
		end   = int(math.floor(math.sqrt(float(B))))
		fair_and_squares = 0
		for palindrome in palindrome_generator(start, end):
			if is_palindrome(palindrome * palindrome):
				#print A, B, start, end, palindrome, palindrome * palindrome
				fair_and_squares += 1
		sys.stdout.write("Case #{}: {}\n".format(test_case+1, fair_and_squares))
