T = input()
for t in range(T):
	input()
	C = map(int,raw_input().split())
	xor = 0
	for c in C:
		xor ^= c
	print "Case #%s: %s" % (t+1,sum(sorted(C)[1:]) if xor==0 else "NO")
