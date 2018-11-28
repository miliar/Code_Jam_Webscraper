def recycle(A,B):
	count =0
	if ( len(A) == 0 and len(B) == 0 ):
		return 0

	intA = int(A)
	intB = int(B)
	
	for i in range(intA,intB+1):
		n = i
		m = i

		slen = len(str(i))
		m = []
		for j in range(slen):
			m.append(str(i)[j])

		for j in range(slen):
			t = m[-1]
			del m[-1]
			m.insert(0,t)

			s = ''
			for c in m:
				s+=c

			if ( int(s) <= intB and int(s) > n and int(s) >= intA ) :
				count+=1

	return count

ncase = int(raw_input())

#recycle('12345','34512')

for icase in range(ncase):
	ip = raw_input().split()
	print 'Case #%d:'%(icase+1),
	print recycle(ip[0],ip[1])
