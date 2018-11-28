# -*- coding: utf-8 -*-
import time

deuce_exps = [2 ** x for x in xrange(1, 100)]
def load_input():
	T = int(raw_input())  # read a line with a single integer
	NK_list = []
	for i in xrange(T):
		N, K = raw_input().split(" ")
		NK_list.append([int(N), int(K)])
	return NK_list
	# print("Case #{}: {} {}".format(i, n + m, n * m))
	# check out .format's specification for more formatting options


def move(S):
	Rs = S / 2
	Ls = max((S - 1) / 2, 0)
	return {'Rs': Rs,'Ls':  Ls}


def solve(NK):
	N, K = NK
	rl_list = []

	CO = 0
	for exp in deuce_exps:
		if K >= exp:
			CO = exp
		else:
			break
	
	while K > 1:
		# Left
		if K > CO + CO / 2 - 1:
			rl_list.append('l')
			K = K - CO
		# Right
		else:
			rl_list.append('r')
			K = K - (CO / 2)
		CO = CO / 2
		# print K, CO
		# time.sleep(1)
	rl_list.reverse()

	# print N,
	for d in rl_list:
		if d == 'r':
			N = move(N)['Rs']
		else:
			N = move(N)['Ls']
		# print N,
	# print rl_list,
	return move(N)


def main():
	NK_list = load_input()
	for i, NK in enumerate(NK_list):
		# print NK,
		result = solve(NK)
		print 'Case #%(i)d: %(Rs)d %(Ls)d' % {
			'i': i+1, 'Rs': result['Rs'], 'Ls': result['Ls']}


if __name__ == '__main__':
	main()
