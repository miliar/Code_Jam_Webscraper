#/usr/bin/python

T = int(raw_input())
for i in range(0, T):
	nm = raw_input().split(' ')
	(n, m) = (int(nm[0]), int(nm[1]))

	dirs = []
	mk_count = 0
	for j in range(0, n):
		s = raw_input().split('/')
		for k in range(0, len(s)):
			s2 = "/".join(s[0:k+1])
			found = False
			for adir in dirs:
				if s2 == adir:
					found = True
			if not found:
				dirs += [s2]
	
	for j in range(0, m):
		s = raw_input().split('/')
		for k in range(0, len(s)):
			s2 = "/".join(s[0:k+1])
			if s2 == '': continue
			found = False
			for adir in dirs:
				if s2 == adir:
					found = True
			if not found:
				dirs += [s2]
				mk_count = mk_count + 1
	print "Case #" + str(i+1) + ": " + str(mk_count)
