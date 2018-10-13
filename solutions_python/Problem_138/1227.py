#! /usr/bin/python

from sys import stdin

def ken_strategy(n_move, k):
	
	for i in k:
		if i>n_move:
			return i

	return k[0]


def get_next_bigget(element, list):

	for i in list:
		if i>element:
			return i

	return -1


def war(n, k):
	
	k.sort()
	score_n = 0

	for n_move in n:
		k_move = ken_strategy(n_move, k)

		if n_move > k_move:
			score_n += 1

		# n.remove(n_move)
		k.remove(k_move)

	return score_n


def d_war(T, n, k):

	n.sort()
	k.sort()
	score_n = 0

	for i in xrange(T):

		x = get_next_bigget(k[0], n)
		if x != -1:
			n_move = x
			n.remove(x)
			k_move = k.pop(0)
			score_n += 1

		else:
			n_move = n.pop(0)
			k_move = ken_strategy(n_move, k)
			k.remove(k_move)

	return score_n


if __name__ == '__main__':
	
	N = int(stdin.readline())
	for i in xrange(N):

		T = int(stdin.readline())
		n = [float(x) for x in stdin.readline().split()]
		k = [float(x) for x in stdin.readline().split()]

		res = war(n, list(k))
		resD = d_war(T, n, list(k))
		print "Case #%d:" % (i+1), resD, res