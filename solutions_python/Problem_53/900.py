#!/usr/bin/env python
# Gerben Stouten
# Google CodeJam Assignment 1C small

def cjr1a2(N,K):
	switch = [0]*(N+1)
	# Minimal amount of clicks needed to reach switch N
	if K<(2**(N-1)): return False
	# Power on|off after K clicks
	for i in range(0,N+1):
		switch[i]=not((K+1)%(2**i))
	if False in switch: return False
	return True

	
if __name__ == "__main__":
	import sys
	for filename in sys.argv[1:]:
		f = open(filename)
		line = f.readline()
		for case in range(int(line)):
			N, K = f.readline().split()[:2]
			print "Case #%i: %s" % (case+1, cjr1a2(int(N),int(K)) and "ON" or "OFF")
