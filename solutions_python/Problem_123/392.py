import sys
inp = sys.stdin

def read_ints():
	return map(int, inp.readline().split())

T=read_ints()[0]
for t in range(T):
	A, N = read_ints()
	ns = read_ints()
	ns.sort()
	ans=0
	best_ans=12345678901234567891234567890123456789
	if A == 1:
		ans = best_ans = len(ns)
		ns=[]
	while ns:
		small=ns[0]
		#print A, ans, ns
		if A > small:
			A+=small
			ns=ns[1:]
		#elif ns[-1] == A:
		#	ans=best_ans=min(best_ans, ans+len(ns))
		#	break
		else:
			best_ans=min(best_ans, ans+len(ns))
			A+=A-1
			ans+=1
	#if best_ans == 12345678901234567891234567890123456789:
	#	best_ans = 0
	#print ans, best_ans
	best_ans=min(best_ans, ans)
	print "Case #%d: %d" % (t+1, best_ans)
