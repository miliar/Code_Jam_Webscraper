import os,sys

DOWNLOADS = "C:\\Users\\vasiliy.strelnikov\\Downloads"

ANSWERS = {}

def solve(P):
	#print "Solve : ", P
	
	if P in ANSWERS:
		#print "In cache: ", ANSWERS[P]
		return ANSWERS[P]

	Pi = [int(c) for c in P]
	
	mx = max(Pi)
	if (mx <= 3):
		ANSWERS[P] = mx
		return mx

	s = mx
	for d in range(len(Pi)):
		for p in range(2, Pi[d] - 1):
			NP = Pi + [p]
			NP[d] = NP[d] - p
			NP.sort()
			ns = 1 + solve("".join([str(np) for np in NP]))
			if ns < s:
				s = ns
				#print s, NP, "! after", P

	NP = [max(0, p - 1) for p in Pi if p > 1]
	ns = 1 + solve("".join([str(np) for np in NP]))
	if ns < s:
		s = ns
		#print s, NP, "! after", P

	ANSWERS[P] = s
	#print "Put in cache for ", P, "=", ANSWERS[P]
	return s

#def solve(P, depth = 0):
#	#print "Solve : ", P, depth
#	mx = max(P)
#	
#	if (mx <= 3):
#		return mx
#
#	mx_ind = P.index(mx)
#	mx_half = mx / 2
#	NP = P + [mx - mx_half]
#	NP[mx_ind] = mx_half
#	return min(mx, 1 + solve(NP))


#def solve(P, depth = 0):
#	#print "Solve : ", P, depth
#	mx = max(P)
#	
#	if (mx <= 3):
#		return mx
#
#	mx_ind = P.index(mx)
#	mx_half = mx / 2
#	NP = P + [mx - mx_half]
#	NP[mx_ind] = mx_half
#	NP2 = [max(0, p - 1) for p in P]
#
#	return min(1 + solve(NP2), 1 + solve(NP))


sel_files = []
for fname in os.listdir(DOWNLOADS):
	if fname[:2] == "B-" and fname[-3:] == ".in":
		print len(sel_files), ":", fname
		sel_files.append(fname)

ix = int(sys.stdin.readline())

infile  = sel_files[ix]
outfile = infile[:-3] + ".out"

ifile = open(DOWNLOADS + "\\" + infile)
ofile = open(DOWNLOADS + "\\" + outfile, "w")

T = int(ifile.readline().strip())
for t in range(T):
	D = int(ifile.readline().strip())
	P = ifile.readline().strip().split()
	P = sorted([int(p) for p in P])

	#Pmax = max(P)
	
	m = solve("".join([str(p) for p in P]))

	ans = "Case #" + str(t+1) + ": " + str(m) #	+ " - " + str(P)
	print ans
	ofile.write(ans + "\n")