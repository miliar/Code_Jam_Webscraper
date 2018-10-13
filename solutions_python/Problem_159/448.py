#!/usr/bin/env python

def main():
	f = open('input.txt', 'r')

	total_T = int(f.readline())

	for T in xrange(1,total_T+1):
		N = int, f.readline().rstrip('\n')
		M = map(int, f.readline().rstrip('\n').split())

		# print find_speed(M)
		print 'Case #{}: {} {}'.format(T, resolve1(M), resolve2(M))


def resolve1(M):
	c = 0
	for x in xrange(0, len(M)-1):
		if M[x] > M[x+1]:
			c += M[x]-M[x+1]

	return c

def resolve2(M):
	v = find_speed(M)

	c = 0
	for x in xrange(0, len(M)-1):
		if M[x] >= v:
			c += v
		else:
			c += M[x]

	return c


def find_speed(M):
	v = 0
	for x in xrange(0, len(M)-1):
		if M[x] > M[x+1]:
			v = max(v, M[x]-M[x+1])

	return v


if __name__ == '__main__':
	main()