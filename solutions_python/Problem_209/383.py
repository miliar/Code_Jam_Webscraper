from math import pi


def solve():
	N,K = map(int, raw_input().split())
	cyls = sorted([map(int,raw_input().split()) for i in xrange(N)])
	cyls.sort(key = lambda cyl: -cyl[1])
	res = 0.0

	for i in range(N):
		rad = cyls[i][0]
		hei = cyls[i][1]
		heis = []
		for j in range(N):
			if j != i and cyls[j][0] <= rad:
				heis.append(cyls[j])
		heis.sort(key = lambda cyl: cyl[0]*cyl[1],reverse=True)

		if len(heis) >= K-1:
			heis = heis[:K-1]
			res = max(res, pi*rad*rad + 2*pi*(sum((cyl[0]*cyl[1] for cyl in heis))+rad*hei) )

	return res


if __name__ == '__main__':
	t = input()
	for i in xrange(1,t+1):
		print 'Case #%d: %.10f' %(i, solve())
