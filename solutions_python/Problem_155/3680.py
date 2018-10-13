fi = open("A-small-attempt1.in",'r')
fo = open("A_small.out",'w')
t = fi.readline()
for i in range(len(t)):
	if t[i] == "\n" or t[i] == " ":
		t = int(t[0:i])
		break
#print t
for i in range(t):
	s = fi.readline()
	s = s.split()
	#print s
	shymax = int(s[0])
	aud = s[1]
	csum = [0]*(shymax+1)
	rp = 0
	for j in range(shymax+1):
		add = 0
		if int(aud[j]) > 0:
			if j>csum[j]:
				rp += j-csum[j]
				add = int(aud[j]) + rp
			else:
				add = int(aud[j])
			pass
		if j<(shymax):
			csum[j+1] = csum[j] + add
	out = "Case #"+str(i+1)+": "+str(rp)
	if i<t-1:
		out = out + '\n'
	#print out
	#print csum
	fo.write(out)