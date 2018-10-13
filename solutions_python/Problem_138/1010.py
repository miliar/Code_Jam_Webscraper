import sys
import numpy as np

def parse_board(fh):
	cases = []
	for _ in xrange(int(next(fh))):
		int(next(fh))  # N
		nmass = sorted(map(float,next(fh).split()))
		kmass = sorted(map(float,next(fh).split()))
		cases.append((nmass, kmass))
	return cases

def solve_case(nmass, kmass):
	dw = solve_dwar(nmass[:], kmass[:])
	return dw, solve_war(nmass, kmass)

def solve_dwar(nmass, kmass):
	score = 0
	while len(nmass) > 0:
		ni = np.searchsorted(nmass, kmass[0])
		if ni == len(nmass):
			ni = 0
			ntold = kmass[-1] - 1e-8
		else:
			ntold = kmass[-1] + 1e-8
		ki = np.searchsorted(kmass, ntold) % len(kmass)
		if nmass[ni] > kmass[ki]:
			score += 1
		nmass.pop(ni)
		kmass.pop(ki)
	return score

def solve_war(nmass, kmass):
	score = 0
	while len(nmass) > 0:
		ni = len(nmass) - 1
		ki = np.searchsorted(kmass, nmass[ni])
		if ki == len(kmass):
			ki = 0
		if nmass[ni] > kmass[ki]:
			score += 1
		nmass = nmass[:-1]
		kmass.pop(ki)
	return score

def main():
	cases = parse_board(sys.stdin)
	for i,case in enumerate(cases):
		y, z = solve_case(*case)
		print "Case #%d: %d %d" % (i+1, y, z)

if __name__ == '__main__':
	main()
