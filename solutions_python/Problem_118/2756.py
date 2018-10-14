

def is_palindrome(x):
	return str(x) == str(x)[::-1]
	
palindromes = filter(is_palindrome, xrange(1000))
squares = map(lambda x: x**2, palindromes)
square_palindromes = filter(is_palindrome, squares)

def count_palindromes(low, high):
	return len(filter(lambda x: True if x >= low and x <= high else False, square_palindromes))


cases = int(raw_input())

for case in range(cases):
	print("Case #{}: {}".format(case+1, count_palindromes(*[int(x) for x in raw_input().split()])))