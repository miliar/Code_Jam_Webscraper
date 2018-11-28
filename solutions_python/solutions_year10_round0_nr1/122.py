for i in xrange(input()):
	n,k = map(int, raw_input().split())
	b = (1<<n)-1
	mode = "ON" if (k&b)==b else "OFF"
	print "Case #%d:"%(i+1), mode