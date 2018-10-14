import sys

def is_tidy(num):
	for i in xrange(len(num) - 1):
		if num[i] > num[i+1]:
			return False
	return True

def get_tidy(num):
	if is_tidy(str(num)):
		return str(num)

	num_str = str(num)
	last_digit = num_str[-1]
	for digit in xrange(int(last_digit), 0, -1):
		new_num = str(int(num_str[:-1] + str(digit)))
		if is_tidy(new_num):
			return new_num
	return get_tidy(int(str(num)[:-1]) - 1) + '9'

lines = [x for x in open(sys.argv[1], 'rt').readlines()]
count = int(lines.pop(0))
with open('out.txt', 'wt') as outfile:
	for i in xrange(count):
		num = int(lines.pop(0).strip())
		res = str(int(get_tidy(num)))
		print 'Case #%d: %s' % (i + 1, res)
		outfile.write('Case #%d: %s\n' % (i + 1, res))
