import sys

T=int(raw_input())
for t in xrange(T):
	data=raw_input().split()
	N=int(data[0])
	L=int(data[1])
	H=int(data[2])
	freqstr=raw_input().split()
	freq=[]
	for i in xrange(len(freqstr)):
		freq+=[int(freqstr[i])]
	main=False
	for f in xrange(L,H+1):
		flag=True
		for i in xrange(len(freq)):
			if freq[i]%f!=0 and f%freq[i]!=0:
				flag=False
				break
		if flag:
			main=True
			break
	sys.stdout.write("Case #%d: " %(t+1))
	if main: print f
	else: print "NO"