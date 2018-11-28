def solve(s,n):
	a=[1 if s[i]=="+" else -1 for i in xrange(len(s))]
	fix = 0
	for i in xrange(len(s)-n+1):
		if a[i]==-1:
			fix += 1
			for j in xrange(i,i+n): a[j]*=-1
	return "IMPOSSIBLE" if sum(a)!=len(s) else str(fix)

testcase = input()
for i in range(testcase):
	S = raw_input().split()
	print "Case #"+str(i+1)+":",solve(S[0],int(S[1]))
