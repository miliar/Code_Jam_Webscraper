from math import *
import bisect

allvals = {}

def readin(fname):
	with open(fname, 'r') as f:
		contents = f.readlines()
	ntrials = int(contents[0])
	trials = [[int(contents[2*i+1]), [int(a) for a in contents[2*i+2].replace('\n','').split(' ')]] for i in range(0, ntrials)]
	return [ntrials, trials]

def solve(cakes):
	h = ','.join(str(x) for x in cakes if x != 0)
	if h in allvals:
		return allvals[h]
	if cakes[-1] == 3:
		return 3
	if cakes[-1] == 2:
		return 2
	if cakes[-1] == 1:
		return 1
	if cakes[-1] == 0:
		return 0
	ncakes = [max(i-1, 0) for i in cakes]
	r = solve(ncakes) + 1
	v = cakes[-1]
	for i in range(2, v-1):
		ncakes2 = cakes[:-1]
		bisect.insort_right(ncakes2, v-i)
		bisect.insort_right(ncakes2, i)
		r2 = solve(ncakes2) + 1
		r = min(r2, r)
	allvals[h] = r
	return r

def maxi(lst):
	m = max(lst)
	return [m, lst.index(m)]

def main():
	[ntrials, trials] = readin('B-small-attempt3.in')
	f = open('answer.out', 'w')
	for i in range(0,ntrials):
		time = solve(sorted(trials[i][1]))
		print trials[i][1], i, time
		f.write('Case #%d: %d\n' % (i+1, time))
	f.close()

if __name__=='__main__':
	main()
