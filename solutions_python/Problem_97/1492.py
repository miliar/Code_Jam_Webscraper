f = open("c-small.in", "r")
din = f.read()
f.close()
din = din.split("\n")[1:]

def yes(n, m):
	n = str(n)
	m = str(m)
	for i in xrange(len(m)+1):
		if n == m: return True
		m = m[1:] + m[0]
	return False

def solve(a, b):
	c = 0
	for n in xrange(a, b+1):
		for m in xrange(n+1, b+1):
			if yes(n, m): c += 1
	return c

sout = ""
nline = 1
for line in din:
	if line == "": continue
	ln = "Case #%d: " % (nline)
	
	a, b = int(line.split(" ")[0]), int(line.split(" ")[1])
	ln += "%d" % solve(a, b)
	sout += ln
	sout += "\n"
	
	print ln
	
	
	nline += 1

f = open("c-small.out", "w")
f.write(sout)
f.close()
#print sout
