# Uses https://github.com/DarioFanucchi/CompetitionCode.git
import sys
sys.path.insert(0, "../../../CompetitionCode")
import codejam_io
from itertools import combinations

def check_links(degL, degR, links):
	linksL = [0]*len(degL)
	linksR = [0]*len(degR)
	for A,B in links:
		linksL[A] += 1
		linksR[B] += 1
	for idx,linkL in enumerate(linksL):
		if linkL >= degL[idx]:
			return False
	for idx,linkR in enumerate(linksR):
		if linkR >= degR[idx]:
			return False
	return True

def solve_small(degL, degR, links):
	Nmax = 0
	for N in xrange(1, len(links)):
		for x in combinations(links, N):
			if check_links(degL, degR, x):
				Nmax = N
				continue 

	return Nmax


def solve_case(c):
	Lvals = sorted(list(set([x[0] for x in c])))
	Rvals = sorted(list(set([x[1] for x in c])))
	L = {x:i for i, x in enumerate(Lvals)}
	R = {x:i for i, x in enumerate(Rvals)}

	c1 = [[L[x[0]], R[x[1]]] for x in c]

	degL = [0]*len(Lvals)
	degR = [0]*len(Rvals)

	for (A,B) in c1:
		degL[A] += 1
		degR[B] += 1

	return solve_small(degL, degR, c1)

def solve(fin, fout):
	L = codejam_io.read_f(fin, lambda x: [str]*x[0])
	S = map(solve_case, L)
	codejam_io.write_simple(fout, S)

#solve("C-sample.in", "C-sample.out")
#solve("C-small-attempt0.in", "C-small-attempt0.out")
#solve("C-small-attempt1.in", "C-small-attempt1.out")
solve("C-small-attempt2.in", "C-small-attempt2.out")
#solve("C-large.in", "C-large.out")