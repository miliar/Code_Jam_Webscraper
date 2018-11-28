import sys

def square_gen(lower, upper):
	i = 1
	i_sq = 1
	while i_sq <= upper:
		if i_sq >= lower:
			yield i_sq
		i += 1
		i_sq = i * i

def palindrome_gen(lower, upper):
	length = 1
	i = 1
	pal = 1
	while pal <= upper:
		if pal >= lower:
			yield pal
		i += 1
		if i >= 10 ** ((length+1)/2):
			length += 1
			if length % 2 == 0:
				i = i/10
		if length % 2 == 0:
			pal = int(str(i) + str(i)[::-1])
		else:
			pal = int(str(i) + str(i)[::-1][1:])

def naive(lower, upper):
	palindromes = list(palindrome_gen(1, upper))
	i = 1
	i_sq = 1
	while i_sq <= upper:
		if i_sq >= lower and i in palindromes and i_sq in palindromes:
			yield i_sq
		i += 1
		i_sq = i * i

def main():
	num_tests = sys.stdin.readline()
	tests = [[int(x) for x in s.split()] for s in sys.stdin.readlines()]
	# returns [[A, B]]

	for i, (A, B) in enumerate(tests):
		ans = len(list(naive(A, B)))
		print "Case #" + str(i+1) + ":", ans

if __name__ == '__main__':
	main()