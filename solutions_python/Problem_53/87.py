import sys

T=int(sys.stdin.readline())
for case in range(T):
	(N,K) = map(int, sys.stdin.readline().split())
	need = 2**N - 1
#	print K, need
	on = (K & need) == need
	print "Case #%d: %s" % (case+1, "ON" if on else "OFF")
	
	