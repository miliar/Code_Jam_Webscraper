import os
import sys
import heapq

global num_tests

# o....o
# o.o..o
# o.oo.o

def create_one(min_stall, max_stall):
	chosen_stall1 = (max_stall + min_stall) / 2
	Ls = chosen_stall1 - min_stall - 1
	Rs = max_stall - chosen_stall1 - 1
	return (-min(Ls, Rs), -max(Ls, Rs), chosen_stall1, min_stall, max_stall)

def solve(l):
	N, K = [int(a) for a in l.split(' ')]
	heap = [create_one(0, N+1)]
	if N == K:
		return "0 0"

	for a in xrange(K):
		min_ls_rs, max_ls_rs, chosen_stall, min_stall, max_stall = heapq.heappop(heap)

		if chosen_stall - min_stall > 1:
			heapq.heappush(heap, create_one(min_stall, chosen_stall))
		if max_stall - chosen_stall > 1:
			heapq.heappush(heap, create_one(chosen_stall, max_stall))

	return '%d %d' % (abs(max_ls_rs), abs(min_ls_rs))

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
		print i
		if s is not None:
			out_fd.write('Case #%d: %s' % (i-1, s))
			out_fd.write('\n')

if __name__ == "__main__":
	main()