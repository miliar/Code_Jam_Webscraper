import sys

def pr(casen,permus):
	print "Case #%s: %s" % (casen,permus)

def cmin(case):
	camin = -1
	rin = -1
	for i in range(len(case)):
		lc = len(case[i])
		if i == 0:
			camin = lc
			rin = i
		if lc>camin:
			camin = lc
			rin = i
	return rin

def solve(case, dic, casen):
	while True:
		#print dic,case
		if not case:
			pr(casen, len(dic))
			return
		if not dic:
			pr(casen, 0)
			return
		lc = len(case)
		min = cmin(case)
		newdic = []
		for w in dic:
			if w[min] in case[min]:
				wnew = w[:min] + w[min+1:]
				newdic.append(wnew)
				continue
		dic = newdic
		case = case[:min]+case[min+1:]

filename = sys.argv[1]

fp = open(filename)

inputs = fp.readline().strip().split()

L,D,N = (int(inputs[0]),int(inputs[1]),int(inputs[2]))

dic = []

for i in range(D):
	dic.append(fp.readline().strip())

for i in range(N):
	case = fp.readline().strip()
	casetokens = []
	cpos = 0
	for j in range(L):
		if case[cpos] != "(":
			casetokens.append(case[cpos])
			cpos = cpos + 1
			continue
		k = cpos+1
		while case[k] != ")":
			k = k + 1
		casetokens.append(case[cpos+1:k])
		cpos = k + 1
	solve(casetokens, dic, i+1)
