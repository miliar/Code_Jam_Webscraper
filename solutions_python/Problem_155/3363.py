T = int(raw_input())
for x in range(0, T):
	line = raw_input().split()
	smax = int(line[0])
	shycounts = list(line[1])
	sc = [ int(i) for i in shycounts ]
	ppl = 0
	for y in range(0, len(sc)-1):
		standing = sum(sc[:y+1])
		if sc[y+1]!=0 and y+1 > standing:
			ppl += (y+1)-standing 
			sc[y] =(y+1)-standing

	print "Case #"+str(x+1)+": " + str(ppl)


