def readInts():
    return [int(x) for x in raw_input().strip().split()]

T = readInts()[0]
for i in xrange(T):
    [n,l,h] = readInts()
    freqs = readInts()
    print "Case #%d:"%(i+1),
    done = False
    res = 0
    for f in range(l,h+1):
	all1 = 0
	for freq in freqs:
	    if (freq % f ==0 or f%freq==0):
		all1+=1
	if (all1 == len(freqs)):
	    done = True
	    res = f
	    break
    if done:
	print f
    else:
	print "NO"
    