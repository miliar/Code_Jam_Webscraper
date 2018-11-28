#!/usr/bin/python
T = int(raw_input())
for t in range(T):
	N,L,H = [int(i) for i in raw_input().split()]
	notes = [int(i) for i in raw_input().split()]
	i = L
	res = "NO"
	while i<=H:
		flag = True
		for n in notes:
			if not ((n%i == 0) or (i%n == 0)):
				flag = False
				#print n,i
				break
		if flag:
			res = i
			break
		i += 1
	
	print "Case #%d: %s" % (t+1, res)