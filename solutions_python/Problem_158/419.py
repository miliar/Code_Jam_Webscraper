import os,sys

DOWNLOADS = "C:\\Users\\vasiliy.strelnikov\\Downloads"

sel_files = []
for fname in os.listdir(DOWNLOADS):
	if fname[:2] == "D-" and fname[-3:] == ".in":
		print len(sel_files), ":", fname
		sel_files.append(fname)

ix = int(sys.stdin.readline())

infile  = sel_files[ix]
outfile = infile[:-3] + ".out"

ifile = open(DOWNLOADS + "\\" + infile)
ofile = open(DOWNLOADS + "\\" + outfile, "w")

T = int(ifile.readline().strip())
for t in range(T):
	(X, R, C) = ifile.readline().strip().split()
	X, R, C = int(X), int(R), int(C)

	if X == 1:
		ans = "GABRIEL"	
	elif X == 2:
		ans = (R*C % 2 == 0) and "GABRIEL" or "RICHARD"
	elif X == 3:
		ans = (R*C % 3 != 0 or R == 1 or C == 1) and "RICHARD" or "GABRIEL"
	elif X == 4:
		ans = (R*C % 4 != 0 or R <= 2 or C <= 2) and "RICHARD" or "GABRIEL"
	
	ans = "Case #" + str(t+1) + ": " + ans
	print ans
	ofile.write(ans + "\n")