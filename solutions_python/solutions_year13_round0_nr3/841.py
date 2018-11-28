import math
import sys

def generate_fairandsquare_numbers(limit):
	pal_limit = int(math.ceil(math.sqrt(limit)))
	pal = generate_palindromes(pal_limit)
	return [x*x for x in pal if is_palindromic(x*x)]

def generate_palindromes(limit):
	result = []
	for i in range(min(10, limit)):
		result.append(i)

	i = 1
	done = False
	while not done:
		done = True
		for mid in [str(x) for x in range(0, 10)] + [""]:
			pal = int(str(i) + mid + str(i)[::-1])
			if pal <= limit:
				done = False
				result.append(pal)
		i += 1

	return result

def is_palindromic(num):
	s = str(num)
	if len(s) == 1:
		return True

	half = int(len(s) / 2)
	return s[:half] == s[-half:][::-1]

def main():
	fas = generate_fairandsquare_numbers(math.pow(10, 14))

	f = open(sys.argv[1], 'r')
	count = int(f.readline())
	for i in range(count):
		minfas, maxfas = [int(x) for x in f.readline().split()]

		print 'Case #' + str(i + 1) + ': ' + str(len([x for x in fas if x >= minfas and x <= maxfas]))

if __name__ == "__main__":
	main()