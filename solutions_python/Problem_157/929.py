import sys
sys.stdin=open('1.in', 'r')
sys.stdout=open('1.out','w')
for t in range(input()):
	n,p=map(int,raw_input().split())
	s=raw_input()*p
	fi=fj=now=0
	sign=1
	for x in s:
		if now==0:
			now=x
		else:
			if now==x:
				sign*=-1
				now=0
			else:
				for ch in 'ijk':
					if ch!=now and ch!=x:
						
						if (now=='i' and x=='k') or (now=='j' and x=='i') or (now=='k' and x=='j'): 
							sign*=-1
						now=ch
						break
		if sign==1:
			if now=='i' and fi==0: 
				fi=1
			elif now=='k' and fi==1 and fj==0: 
				fj=1				 
		#print x, now, fi, fj, sign
	ans='YES' if fi and fj and now==0 and sign==-1 else 'NO'
	print 'Case #%d:'% (t+1), ans