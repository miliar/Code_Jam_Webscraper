#!/usr/bin/env python

def main():
	f = open('input.txt', 'r')

	total_T = int(f.readline())

	for T in xrange(1,total_T+1):
		a1 = int(f.readline())
		a1v = []
		a1v.append(map(long, f.readline().rstrip('\n').split()))
		a1v.append(map(long, f.readline().rstrip('\n').split()))
		a1v.append(map(long, f.readline().rstrip('\n').split()))
		a1v.append(map(long, f.readline().rstrip('\n').split()))

		a2 = int(f.readline())
		a2v = []
		a2v.append(map(long, f.readline().rstrip('\n').split()))
		a2v.append(map(long, f.readline().rstrip('\n').split()))
		a2v.append(map(long, f.readline().rstrip('\n').split()))
		a2v.append(map(long, f.readline().rstrip('\n').split()))

		# print a1, a1v
		# print a2, a2v

		a1s = set(a1v[a1-1])
		a2s = set(a2v[a2-1])
		r = a1s&a2s

		if len(r)==1:
			rs = list(r)[0]
		elif len(r)>1:
			rs = 'Bad magician!'
		else:
			rs = 'Volunteer cheated!'

		# print E,R,N
		# print v

		print 'Case #{}: {}'.format(T, rs)


if __name__ == '__main__':
	main()