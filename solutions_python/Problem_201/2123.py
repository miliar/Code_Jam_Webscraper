t = int(raw_input())  # read a line with a single integer


for i in xrange(1, t + 1):
  N,K = [ int(s) for s in raw_input().split(" ")]
  y=z=0

  empty=[N]
  while K>0:
	N = empty.pop()
	if N%2 == 0: 
		y = (N/2)-1
	else: 
		y = (N//2)
	z=N-y-1
	if z < 0 : z=0
	if y < 0: y = 0
	
	if z == 0 and y == 0 : break 
	empty.append(z)
	empty.append(y)
	empty=sorted(empty)
	K=K-1
	
	z=max(z,y)
	y=min(z,y)
  print "Case #{}: {} {}".format(i, z,y)	
  #if i == 4 : exit(0)