#!/usr/bin/env python

def takeRound(k, n, lidx, gs):
	sm = 0
	for i in range(n):
		if sm + gs[lidx[i]] > k:
			break
		sm += gs[lidx[i]]
	#	print i, gs[lidx[i]]
	if i >= n:
		nh = lidx[0]
	else:
		nh = lidx[i]
#	print "new head %d, make mony %d" % (nh, sm)
	return nh, sm


def findLoop(r, k, n, gs):
	heads = []
	loop = []
	s = 0
	nh = 0
	bloop = False
	i = 0

	while not bloop and i < r:
		heads.append(nh)
		lidx = range(n)
		lidx = lidx[nh:] + lidx[:nh]
		nh, sm = takeRound(k, n, lidx, gs)
		loop.append(sm)

		try:
			s = heads.index(nh)
		except ValueError:
			bloop = False
		else:
			bloop = True
			#print "loop found start from round %d" % s
		r+=1
		#print heads
	return s, len(heads)-s, loop


def solve(r, k, n, gs):
	s, ln, loop = findLoop(r, k, n, gs)
	lcount = (r-s) // ln
	left = (r-s) % ln
	return sum(loop[:s]) + \
			sum(loop[s:])*lcount + \
			sum(loop[s:s+left])


def solveCase():
	r, k, n = [eval(x) for x in raw_input().split(' ')]
	gs = [eval(x) for x in raw_input().split(' ')]
	return solve(r, k, n, gs)


def outputCase(i):
	print "Case #%d: %s" % (i+1, solveCase())

def main():
	ncase = input()
	for i in xrange(ncase):
		outputCase(i)

if __name__ == "__main__":
	main()
