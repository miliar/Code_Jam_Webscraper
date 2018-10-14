import sys
import math

def get_intervals():
	lines = sys.stdin.read().split('\n')[1:-1]
	interval_strings = [line.split(' ') for line in lines]
	return [(int(line[0]),int(line[1])) for line in interval_strings]

def get_palindromes(low_bound,high_bound):
	def is_palindrome(num):
		if len(str(num)) == 1: return True
		if len(str(num)) == 2: return str(num)[0]==str(num)[1]
		left = str(num)[:len(str(num))/2]
		if len(str(num)) % 2 == 0:
			right = str(num)[len(str(num))/2:][::-1]
		else:
			right = str(num)[len(str(num))/2 + 1:][::-1]
		return left == right
			
	palindromes = []
	for x in range(low_bound,high_bound + 1):	
		if is_palindrome(x): palindromes.append(x)
	return palindromes

def get_fair_and_square(low_bound,high_bound):
	palindromes = get_palindromes(low_bound,high_bound)
	others = get_palindromes(1,low_bound-1)
	fair_and_square = []
	for p in palindromes:
		test = math.sqrt(p)
		if int(test)==test and (int(test) in palindromes or int(test) in others):
			fair_and_square.append(p)
	return fair_and_square


def main():
	intervals = get_intervals()
	winners = []
	for i in range(len(intervals)):
		print "Case #%d: %d" % (i+1, len(get_fair_and_square(intervals[i][0],intervals[i][1])))
	
if __name__ == "__main__":
	main()
