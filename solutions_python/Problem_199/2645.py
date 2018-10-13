 
 # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  m=int(m)
  #make n to binary 
  n=n.replace('+','0')
  n=n.replace('-','1')
  NewN=list(n)
  count=0
  if('1' not in n):
  	  print "Case #{}: {}".format(i,  0)
  else:
  	size= len(NewN)

  	for j in range(0,size-m+1):
  		
  		if(NewN[j]=='1'):
  			count=count+1
  			for k in range(j,j+m):
  				if (NewN[k]=='1'):
  					NewN[k]='0'
  				else:
  					NewN[k]='1'

  		
  	if('1' not in NewN):
  	  	print "Case #{}: {}".format(i, count)
  	else: 
  		print "Case #{}: {}".format(i, "IMPOSSIBLE")
  

 