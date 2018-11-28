#!/usr/bin/python

name = 'A-large'

def solve(X, S, R, t, N, B, E, w):
	speed = [0.0]*101
	totalWalks = 0
	for i in xrange(N):
		walk = E[i]-B[i]
		speed[w[i]] += walk
		totalWalks += walk
	speed[0] = float(X-totalWalks)
	res = 0.0
	for i in xrange(101):
		if speed[i] == 0: continue
		if t > 0:
			if t > speed[i]/(R+i):
				t -= speed[i]/(R+i)
				res += speed[i]/(R+i)
				continue
			else:
				speed[i] -= t*(R+i)
				res += t
				t = 0
		res += speed[i]/(S+i)
	return res

fin = open(name+'.in')
fout = open(name+'.out', 'w')

T = int(fin.readline().strip())
for i in xrange(T):
	X, S, R, t, N = (int(n) for n in fin.readline().strip().split(' '))
	B=[]; E=[]; w=[]
	for j in xrange(N):
		Bj, Ej, wj = (int(n) for n in fin.readline().strip().split(' '))
		B.append(Bj); E.append(Ej); w.append(wj)
	res = solve(X, S, R, t, N, B, E, w)
	fout.write('Case #%s: %s\n' % (i+1, res))

fin.close()
fout.close()
