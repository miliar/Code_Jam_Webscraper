import math

t = int(raw_input()) 
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]
  m=m-1
  d={}
  if n%2==0:
  	d[n/2-1] = 1
  	d[n/2] = 1
  else :
  	d[n/2]=2
  max_curr_gap,l,r = n/2,n/2,n/2
  if m==0:
  	if n%2==0:
  		l=n/2-1
  #print d,max_curr_gap
  while(m>0):
  	
  	if max_curr_gap%2==0 :
  		if max_curr_gap/2-1 > 1:
	  		if max_curr_gap/2-1 in d.keys():
	  			d[max_curr_gap/2-1] = d[max_curr_gap/2-1] +1 
	  		else:
	  			d[max_curr_gap/2-1] = 1
	  	if max_curr_gap/2 in d.keys():
  			d[max_curr_gap/2] = d[max_curr_gap/2] + 1
  		else:
  			d[max_curr_gap/2] = 1
  	else :
  		if max_curr_gap/2 in d.keys():
  			d[max_curr_gap/2] = d[max_curr_gap/2] + 2
  		else:
  			d[max_curr_gap/2] = 2
  	if max_curr_gap%2==0:
  		l=max_curr_gap/2-1
  		r = max_curr_gap/2
  	else:
  		l=max_curr_gap/2
  		r=max_curr_gap/2
  	if d[max_curr_gap] > 1:
  		d[max_curr_gap] = d[max_curr_gap]-1
  	else:
  		del d[max_curr_gap]
  		max_curr_gap=max(d.keys(), key=int)
  	
  	if l<0:
  		l=0
  	if r<0:
  		r=0
	#print d,max_curr_gap
	m=m-1
  	if len(d) ==1 and (1 in d.keys()) and m>0:
		l,r=0,0
		break
  	
  print "Case #{}: {} {}".format(i,max(r,l),min(r,l))
  