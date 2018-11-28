import sys

def solve(c, f, x):
	res = x / 2

	tmp = 0.0
	for i in range(1, int(x)//int(c)+1):
		cps = (2 + (i-1)*f)
		tmp += c/cps
		
		cps += f
		if tmp + x/cps < res:
			res = tmp + x/cps
	
	
	
	return res


res = []
with open(sys.argv[1], 'r') as fin:
	caseNo = int(fin.readline())

	for i in range(caseNo):
		g = [float(k) for k in fin.readline().split(' ')]

		res.append(solve(g[0], g[1], g[2]))


with open(sys.argv[1].replace("in", "out").replace("txt", "out"), 'w') as fout:
	for i in range(len(res)):
		fout.write("Case #" + str(i+1) + ": {:.7f}\r\n".format(res[i]))
