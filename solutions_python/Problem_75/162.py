from collections import defaultdict
def Main():
	for case in range(1,1+int(raw_input())):
		inp=[x.strip() for x in raw_input().split()]
		C=int(inp[0])
		D=int(inp[C+1])
		N=int(inp[C+D+2])
		com,opp,inv=inp[1:C+1],inp[C+2:C+D+2],inp[C+D+3:]
		D1,D2={},defaultdict(str)
		for x in com:
			D1[x[0]+x[1]]=x[2]
			D1[x[1]+x[0]]=x[2]
		for x in opp:
			D2[x[0]]+=x[1]
			D2[x[1]]+=x[0]
#		print D1,D2
		ans=[]
		for c in str(inv[0]):
			if(ans and D1.has_key(ans[-1]+c)):
				ans[-1]=D1[ans[-1]+c]
			else:
				# See if list can be cleared
				if( any(cc in ans for cc in D2[c]) ):ans=[]
				else:ans.append(c)
		print 'Case #{0}:'.format(case),
		print '['+', '.join(ans)+']'

Main()

