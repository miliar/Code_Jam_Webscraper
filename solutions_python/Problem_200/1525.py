def solve(info):
	n=map(int,list(info))
	return ''.join(map(str,recurse(n)))

def recurse(n):
	if n[0]==0:
		n.pop(0)
	prev=0
	for x in xrange(0,len(n)):
		if n[x]<prev:
			n[x-1]=n[x-1]-1
			for z in xrange(x,len(n)):
				n[z]=9
			return recurse(n)
		prev=n[x]
	return n


if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases + 1):
		info = raw_input()
		print("Case #%i: %s" % (caseNr, solve(info)))
