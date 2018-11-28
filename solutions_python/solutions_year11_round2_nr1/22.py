import sys

def readg():
	while True:
		line = sys.stdin.readline()
		if line == "":
			return
		tokens = line.strip().split()
		for i in tokens:
			try:
				i = int(i)
			except:
				pass
			yield i

input = readg()
read = input.next

def readm(n):
	for i in range(n):
		yield read()


t = input.next()

def solve():
	n = read()
	x = []
	for i in range(n):
		x += [read()]
	
	wp = []
	for i in range(n):
		tx = x[i]
		wp += [tx.count("1")*1.0/(tx.count("0") + tx.count("1"))]
	owp = []
	for i in range(n):
		twp = []
		for id, c in enumerate(x[i]):
			if c != '.':
				tx = list(x[id])
				tx[i] = '.'
				tx = "".join(tx)
				twp += [tx.count("1")*1.0/(tx.count("0") + tx.count("1"))]
		owp += [sum(twp)/len(twp)]
	oowp = []
	for i in range(n):
		twp = []
		for id, c in enumerate(x[i]):
			if c != '.':
				twp += [owp[id]]
		oowp += [sum(twp)/len(twp)]

	res = "\n"
	for i in range(n):
		res += "{}\n".format(wp[i]*0.25 + owp[i]*0.5+oowp[i]*0.25)

	return res[:-1]

for i in range(t):
	print "Case #{}: {}".format(i+1, solve())
