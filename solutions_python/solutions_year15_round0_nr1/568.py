import os,sys

def ovation(S):
	standing = S[0]
	for i in range(1, len(S)):
		if standing < i:
			return False
		standing = standing + S[i]
	return True


DOWNLOADS = "C:\\Users\\vasiliy.strelnikov\\Downloads"

sel_files = []
for fname in os.listdir(DOWNLOADS):
	if fname[:2] == "A-" and fname[-3:] == ".in":
		print len(sel_files), ":", fname
		sel_files.append(fname)

ix = int(sys.stdin.readline())

infile  = sel_files[ix]
outfile = infile[:-3] + ".out"

ifile = open(DOWNLOADS + "\\" + infile)
ofile = open(DOWNLOADS + "\\" + outfile, "w")

T = int(ifile.readline().strip())
for t in range(T):
	(Smax, S) = ifile.readline().strip().split()
	Smax = int(Smax)
	S = [ord(c) - ord('0') for c in S]

	#print S
	#print "Ovation = " + str(ovation(S))
	
	standing = S[0]
	needed = 0
	for i in range(1, Smax + 1):
		#print i, standing, needed
		if standing >= i:
			standing = standing + S[i]
		else:
			needed = needed + (i - standing)
 			standing = i + S[i]

	ans = "Case #" + str(t+1) + ": " + str(needed)
	print ans
	ofile.write(ans + "\n")