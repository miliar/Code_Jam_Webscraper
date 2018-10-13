import bisect

t = int(raw_input())  # read a line with a single integer
for tt in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]
  st=[0,n+1]
  
  mi=n
  ma=0
  new=0
  gap=0
  gend=0
  gsize=0

  while k:
  	gap=0
  	gend=0
  	gsize=0
  	for i,x in enumerate(st):
  		if i>0 and x-st[i-1]-1 > gap:
  			gap=x-st[i-1]-1
  			gsize,gend=(gap,x)
  	new=gend-(gap+1)/2
  	bisect.insort_left(st,new)
  	k-=1
  	#print st
  
  ind=st.index(new)
  lef=st[ind-1]
  rig=st[ind+1]
  ma=max(rig-new-1,new-lef-1)
  mi=min(rig-new-1,new-lef-1)
  			


  print "Case #{}: {} {}".format(tt, ma, mi)
  #