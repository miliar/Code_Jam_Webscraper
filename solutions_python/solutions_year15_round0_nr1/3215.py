t = input()

for x in xrange(t):
	smax, s = raw_input().split()
	standing = int(s[0])
	invites = 0
	for y in xrange(1, len(s)):
		if(standing >= y):
			if(s[y] == 0):
				pass	
			standing += int(s[y])
		else:
			invites += (y - standing)
			standing += ((y-standing) + int(s[y]))	
	print "Case #%d: "%(x+1) + str(invites)