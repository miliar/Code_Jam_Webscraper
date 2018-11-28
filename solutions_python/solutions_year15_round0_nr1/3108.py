with open("A-large.in") as f:
    content = f.read().splitlines()

T = int(content[0])

# problem A
for x in xrange(1, T+1):
	s = content[x].split(" ")
	li = [int(i) for i in list(s[1])]
	rs = 0
	currentNeededAu = 0
	for i in xrange(0, len(li)):
		if rs >= i:
			rs += li[i]
		else:
			currentNeededAu += i - rs
			rs = i + li[i]
	print "Case #%d: %d" % (x, currentNeededAu)

# problem B
