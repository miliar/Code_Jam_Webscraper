def solve(n):
	a=map(int,list(str(n)))
	r=[]
	for i in xrange(len(a)-1):
		if a[i+1]>=a[i]:
			r.append(a[i])
		elif a[i]>1:
			for j in xrange(len(r)):
				if r[j] > a[i]-1: return r[:j] + [a[i]-1] + [9]*(len(a)-j-1)
			return r + [a[i]-1] + [9]*(len(a)-i-1)
		else:
			return [9]*(len(a)-1)
	return r + [a[-1]]
testcase = input()
for i in range(testcase):
    print "Case #"+str(i+1)+":","".join(map(str,solve(input())))
