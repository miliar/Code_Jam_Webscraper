import sys
fname = sys.argv[1]
with open(fname) as fp:
	lines = [line.strip() for line in fp]

cases = int(lines.pop(0))
cases = range(1,cases+1)
for line, case in zip(lines, cases):
	pre = "Case #%s:" % case
	line = [int(l) for l in line.split()]
	n, s, p = int(line.pop(0)),int(line.pop(0)),int(line.pop(0))
	res = 0
	# minimum scores to satisfy p that is not surprising
	nsmin = p*3-2
	potentials = 0
	smin = (p-2)*3+2

	for scores in line:
		if scores < p:
			continue
		if nsmin<=scores:
			res+=1
			continue
		# can we satisfy if surprising?
		if scores>=smin:
			potentials+=1
			continue
	res += min(potentials,s)

	print pre, res
