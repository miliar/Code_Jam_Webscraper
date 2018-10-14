import sys

def getLine():
	global fin
	line = fin.readline()
	if line[-1]=="\n":
		line = line[:-1]
	return line


def solve(s,queries):
	cost = [[0]+[None for i in queries] for j in xrange(s)]
	for i,q in enumerate(queries):
		for j in xrange(s):
			res = 1e10
			if j!=q:
				for k in xrange(s):
					if k==j:
						res = min(res, cost[j][i])
					else:
						res = min(res, cost[k][i]+1)
			cost[j][i+1] = res

#	print "------"
#	for c in cost:
#		print c
	return str(min(c[len(queries)] for c in cost))
#########
if len(sys.argv) != 2:
	print "Specify input file"
	exit(1)

fin = open(sys.argv[1])


n = int(getLine())

fout = open("out","wt")

for i in range(n):
	print i
	s = int(getLine())
	engines = []
	for j in range(s):
		engines.append(getLine())
	engineNo = dict((e,i) for i,e in enumerate(engines))
	res = [0]*s
	q = int(getLine())
	queries = []
	for j in range(q):
		query = getLine()
		queries.append(engineNo.get(query,-1))
	
	fout.write("Case #%s: "%(i+1))
	fout.write(solve(s,queries))
	fout.write("\n")

fout.close()