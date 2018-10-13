import os
import sys

def solve(l):
	nums = [int(a) for a in l.split(' ')]
	num = nums[0]
	nums = nums[1:]
	nums = [nums[0], nums[2], nums[4]]
	cur = 0
	mapping = 'RYB'
	maxi = max(nums)
	maxi_type = nums.index(maxi)
	nums[maxi_type] = 0
	circle = [maxi_type * maxi]
	if sum(nums) < maxi:
		print nums
		return 'IMPOSSIBLE'

	return interleave(mapping[maxi_type]*maxi, ''.join(mapping[i]*a for i,a in enumerate(nums)))

def interleave(s1,s2):
	l = list(s1)
	for i,a in enumerate(s2):
		l[i % len(l)] += a
	return ''.join(l)

def process_line(l, i):
	global num_tests,num_horses,distance,horses
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
	case_num = 0
	for line in lines:
		s = process_line(line, i)
		i += 1
		if s is not None:
			case_num += 1
			out_fd.write('Case #%d: %s' % (case_num, s))
			out_fd.write('\n')

if __name__ == "__main__":
	main()