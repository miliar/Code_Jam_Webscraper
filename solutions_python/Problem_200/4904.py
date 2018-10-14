def main():
	infile = 'B-small-attempt3.in'
	outfile = 'B-small-attempt3.out'

	f = open(infile, 'r')
	o = open(outfile, 'w')

	num_of_cases = f.readline()

	for i in range(int(num_of_cases)):
		test_num = f.readline()
		largest_tidy_num = getLargestTidy(int(test_num))
		o.write('Case #{}: {}\n'.format(i+1, str(largest_tidy_num)))

	print "Done!"
	o.close()

def getLargestTidy(n):
	if n == 1:
		return 1
	for i in range(n, 1, -1):
		if (isTidy(i)):
			return i

def isTidy(n):
	n = ''.join(reversed(str(n)))
	counter_num = n[0]
	for i, c in enumerate(n):
		if int(counter_num) < int(c):
			return False
		counter_num = c

	return True

if __name__ == '__main__':
	main()