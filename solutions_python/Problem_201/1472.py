def solve(info):
	(n,k)=map(int,info.split(" "))
	s=[n]
	pi=0
	for _ in xrange(0,k):
		t=0
		i=0
		for a2 in xrange(0,len(s)):
			if s[a2]>t:
				t=s[a2]
				i=a2
		s.insert(i,(s[i]-1)//2)
		s[i+1]=(s[i+1])//2
		pi=i
		#print(s)
	return str(max(s[pi],s[pi+1]))+' '+str(min(s[pi],s[pi+1]))

if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases + 1):
		info = raw_input()
		print("Case #%i: %s" % (caseNr, solve(info)))
