lala = int(raw_input())

for aaa in xrange(lala):
	p, k, l = map(int, raw_input().split())
	keys = map(int, raw_input().split())
	keys.sort()
	keys.reverse()
	count = 0
	xxx = 1
	a = 0
	for key in keys:
		count += key * xxx
		a += 1
		if a == k:
			a = 0
			xxx += 1
	print "Case #%s: %s" % (aaa + 1, count) 
	
