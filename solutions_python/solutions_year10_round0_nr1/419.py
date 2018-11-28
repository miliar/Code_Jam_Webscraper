import sys

i = 0
for l in file(sys.argv[1]):
	if i == 0 :
		i += 1
		continue
	(N,K) = l.split(" ")
	N,K = int(N),int(K)
	if K % 2**N == 2**N -1 :
		print "Case #%d: ON" % (i)
	else :
		print "Case #%d: OFF" % (i)
	i += 1
