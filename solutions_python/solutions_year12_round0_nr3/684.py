N = input()
for i in range(N):
	line = raw_input().split()
	A = int(line[0])
	B = int(line[1])

	acum = 0
	for n in range(A, B):
		s = str(n)
		ms = []
		for j in range(1,len(s)):
			if s[j] != '0':
				m = int( s[j:] + s[:j] )
				if m not in ms:
					ms.append(m)
					if m > n and m <= B :
						acum += 1
	
	print "Case #" + str(i+1) + ": " + str(acum)