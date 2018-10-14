from __future__ import print_function
import sys


precomp = {
	3: {2: (0, 0)},
	4: {2: (1,0), 3: (0,0)},
	5: {2: (1,0), 3:(1, 0), 4:(0,0)},
	6: {2:(1,1),3:(1,0),4:(0,0),5:(0,0)},
	7: {2:(1,1),3:(1,1),4:(0,0),5:(0,0), 6:(0,0)},
	8: {2:(2,1),3:(1,1),4:(1,0),5:(0,0), 6:(0,0), 7:(0,0)},
	9: {2:(2,1),3:(2,1),4:(1,0),5:(1,0), 6:(0,0), 7:(0,0), 8:(0,0)},
	10: {2:(2,2),3:(2,1),4:(1,0),5:(1,0), 6:(1,0), 7:(0,0), 8:(0,0), 9:(0,0)},
	11: {2:(2,2),3:(2,2),4:(1,0),5:(1,0), 6:(1,0), 7:(1,0), 8:(0,0), 9:(0,0), 10:(0,0)},
	12: {2:(3,2),3:(2,2),4:(1,1),5:(1,0), 6:(1,0), 7:(1,0), 8:(0,0), 9:(0,0), 10:(0,0), 11:(0,0)},
	13: {2:(3,2),3:(3,2),4:(1,1),5:(1,1), 6:(1,0), 7:(1,0), 8:(0,0), 9:(0,0), 10:(0,0), 11:(0,0), 12:(0,0)},
}


def solve_tc(n, k):
	if k == n:
		return (0, 0)

	if k == 1:
		if n % 2 == 0:
			return (n/2, n/2-1)
		else:
			return (n/2, n/2)

	if n in precomp:
		return precomp[n][k]
	n -= 1
	s1, s2 = solve_tc(n - n/2, k - k/2), solve_tc(n/2, k/2)
	return max(s1, s2)

def another_solve(n, k):
	if k == n:
		return (0, 0)

	positions = []
	for i in xrange(k):
		extended_pos = [0] + positions + [n+1]
		max_val = (-1, -1)
		max_idx = 0
		max_pos = 0
		for j in xrange(len(extended_pos) - 1):
			# import pdb; pdb.set_trace()
			left, right = extended_pos[j], extended_pos[j+1]
			middle = (right - left - 1) / 2
			val = (middle, middle)
			if (right - left - 1) % 2 == 0:
				val = (middle, middle - 1)
			if val > max_val:
				max_val = val
				max_idx = j
				max_pos = left + val[1] + 1
		positions = positions[:max_idx] + [max_pos] + positions[max_idx:]
	return max_val


if __name__ == '__main__':
	# read data
	filename = sys.argv[1]

	with open(filename, 'r') as in_file, open(filename.replace('in', 'out'), 'w') as out_file:
		tc_count = int(in_file.readline())
		for i in range(tc_count):
			n, k = in_file.readline().split()
			k, n = int(k), int(n)
			sol = solve_tc(n, k)
			# sol = another_solve(n, k)

			print('For %d %d ---> %d %d' % (n, k, sol[0], sol[1]))
			print('Case #%d: %d %d' %(i+1, sol[0], sol[1]), file=out_file)

