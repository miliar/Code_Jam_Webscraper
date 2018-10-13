infile = open('A-small-attempt1.in')
outfile = open('out.txt', 'w')
for r in xrange(int(infile.readline().strip())):
	ans = 'impossible'
	p,q = [int(x) for x in infile.readline().strip().split('/')]
	if q==2 or q==4 or q==8 or q==16 or q==32 or q==64 or q==128 or q==256 or q==512 :
		for i in xrange(39):
			p *=2
			if p >= q:
				ans = i + 1
				break

	outfile.write('Case #%d: %s\n' % (r+1, str(ans)))