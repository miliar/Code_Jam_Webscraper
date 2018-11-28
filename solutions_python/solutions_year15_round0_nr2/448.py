# -*-coding:utf8 -*
from parsing import TextGen
infile = "b.in"
outfile = "b.out"

########################
def cutdiv(a, b):
    return -(-a // b) - 1

def algo(inp):
	n_diners = inp.int
	l_diners = [inp.int for _ in range(n_diners)]
	max_cut = max(l_diners)
	score = max_cut
	for try_cut in range(1,max_cut+1):
		try_score = try_cut
		for pank in l_diners:
			try_score += cutdiv(pank,try_cut)
		score = min(score, try_score)
	return score
	


########################

inp = TextGen(infile)
cases = inp.int
with open(outfile,'w') as outdata:
	for case in range(1, cases+1):
		outdata.write("Case #%d: %s\n" % (case, algo(inp)))
