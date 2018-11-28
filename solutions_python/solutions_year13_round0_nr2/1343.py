#import collections

def parse_line(file):
        line = []
        line = file.readline()
        line = line.split()
        line = [int(t) for t in line]
        return line

def is_possible(N, rs, M, cs):
	for r in range(N):
		for c in range(M):
			if rs[r][c] < max(rs[r]) and cs[c][r] < max(cs[c]):
				return False
	return True	

#f = open('./ex.txt', 'r')
f = open('./B-large.in', 'r')
f_results = open('./result.txt', 'w')

cases = int(f.readline())

for case in range(cases):
#	print ""
#	print "Case " + str(case + 1)

        tt = list(parse_line(f))
        N = tt[0]
        M = tt[1]

	lawnX = []
	for t in range(N):
		lawnX.append(parse_line(f))
#	print lawnX
	
	lawnY = []
	for t in range(M):
		tt1 = []
		for tt2 in lawnX:
			tt1.append(tt2[t])		
		lawnY.append(tt1[:])
#	print lawnY

	if is_possible(N, lawnX, M, lawnY):
		results = "YES"
	else:
		results = "NO"

        f_results.write("Case #" + str(case + 1) + ": " + results + "\n")
