INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large.out'

#INPUT_FILE = 'A-small-attempt0.in'
#OUTPUT_FILE = 'A-small-attempt0.out'

#INPUT_FILE = 'sample.in'
#OUTPUT_FILE = 'sample.out'


def solve(s_max, s_counts):
	result = 0
	total = 0
	for i in xrange(s_max+1):
		extra_audience = max(i - total, 0)
		result += extra_audience
		total += s_counts[i]
		total += extra_audience
	return result


def main():
    f_in = open(INPUT_FILE, 'r')
    f_out = open(OUTPUT_FILE, 'w')
    T = int(f_in.readline())
    for t in xrange(T):
        tokens = f_in.readline().split()
        result = solve(int(tokens[0]), [int(s) for s in tokens[1]])
        f_out.write('Case #%d: %d\n' % (t+1, result))
    f_out.close()
    f_in.close()

if __name__ == '__main__':
    main()