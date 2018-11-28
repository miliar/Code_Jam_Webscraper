'''
Dancing With the Googlers - large
Mehdi Yeganeh
Google CodeJam 2012
'''
T = int(raw_input())

for tc in range(0, T):
	input = raw_input().split(' ')
	n = int(input[0])
	s = int(input[1])
	p = int(input[2])
	r=0
	ns=0
	for nt in range(0, n):
		triplet=int(input[3+nt])
		if ((p*3)-2) <= triplet:
			r += 1
		elif ((p*3)-4<=triplet) and (2<=triplet):
			ns += 1
	
	if s>0 and s<=ns:
		r += s
	elif s>0 and s>ns:
		r += ns
			
	print "Case #" + str(tc+1) + ": " + str(r)
	