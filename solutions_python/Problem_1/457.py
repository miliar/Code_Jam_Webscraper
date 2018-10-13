
import sys

if len(sys.argv)>1:
  f=open(sys.argv[1],'r').read().split('\n')
else:
  f="""2
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol""".split('\n')
N=int(f[0])
f=f[1:]

branches={}

for case in range(N):
	switches=0
	S = f[1:int(f[0])+1]
	f=f[int(f[0])+1:]
	Q = f[1:int(f[0])+1]
	f=f[int(f[0])+1:]
	branches={}
	for p in S:
		branches[p]=0
		
	for p in Q:
		if p in branches:
			s=branches[p]+1
			del(branches[p])
			for o in S:
				if o!=p:
					if o in branches:
						branches[o]=min(branches[o],s)
					else:
						branches[o]=s
			
	switches=min(branches.values())
	
	print "Case #%i: %i"%(case+1,switches)




