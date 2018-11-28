import os
import sys

global num_tests

def solve(l):
	num = l
	print "AAAAAAAAAAA", l
	if len(l) == 1:
		return l
	for a in xrange(1,len(l)):
		print a, l[a-1], l[a]
		if l[a-1] > l[a]:
			b = a-1
			while b > 0 and l[b] == l[a-1]:
				b -= 1

			if l[b] == l[a-1]:
				out = l[:b] + chr(ord(l[b]) - 1) + '9'*(len(l) - b-1)
			else:
				b = b+1
				out = l[:b] + chr(ord(l[b]) - 1) + '9'*(len(l) - b-1)
			out = out.lstrip('0')
			return out

	return l

def solve1(l):
	num = int(l)
	tot = 0
	max_one = 1
	for a in xrange(1,num+1):
		s = str(a)
		if s == ''.join(list(sorted(s))):
			max_one = a
	return max_one

def process_line(l, i):
	if i == 0:
		num_tests = int(i)
	else:
		return solve(l)

def main():

	fn = sys.argv[1]
	fn_out = sys.argv[2]
	lines = open(fn, 'rb').read().splitlines()
	out_fd = open(fn_out, 'wb')
	i = 0
	for line in lines:
		s = process_line(line, i)
		i += 1
		if s is not None:
			out_fd.write('Case #%d: %s' % (i-1, s))
			out_fd.write('\n')

if __name__ == "__main__":
	main()