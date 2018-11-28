
T = int(raw_input())
for k in range(T):
  c = 0
  l = (raw_input()).split()
  A, B = int(l[0]), int(l[1])
  for j in range(A, B+1):
    s = str(j)
    d = {}
    for i in range(1, len(s)):
      h = int(s[i:]+s[:i])
      if h > j and h <= B:			
        if h not in d.keys():
	  d[h] = 0
   	  c=c+1	
			
  print "Case #%d: %d" %(k+1, c) 

		

