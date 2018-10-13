from math import log

t=int(raw_input())

def diff(n, lvl):
	if lvl==0:
		return 1 if n%2==0 else 0
	d1=(n-1)/2
	d2=(d1+1) if n%2==0 else d1
	return diff(d1, lvl-1)+diff(d2, lvl-1)

for i in xrange(t):
	n, k=map(int, raw_input().strip().split())

	if k==1:
		ls=(n-1)/2
		rs=ls if n%2==1 else ls+1
		print "Case #"+str(i+1) + ": "+str(rs) + " "+str(ls) 
		continue

	lvl=int(log(k, 2))

	seats=n-(2**lvl - 1)

	divs=2**lvl
	to_seat=k-2**lvl+1

	a = seats/divs

	diff1=diff(n, lvl-1)

	if seats==a*diff1+(a+1)*(divs-diff1):
		if to_seat>(divs-diff1):
			ls=(a-1)/2
			rs=ls if a%2==1 else ls+1
		else:
			ls=a/2
			rs=ls if a%2==0 else ls+1
	else:
		if to_seat > diff1:
			ls=(a-1)/2
			rs=ls if a%2==1 else ls+1
		else:
			ls=a/2
			rs=ls if a%2==0 else ls+1
	print "Case #"+str(i+1) + ": "+str(rs) + " "+str(ls)