t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  turning_point=False
  for n in raw_input().split(" "):
    n = list(n)
    if len(n)>1:
      idx=0
      while idx<len(n):
        if turning_point:
          n[idx]='9'
        elif idx+1<len(n) and n[idx] > n[idx+1]:
          turning_point=True
          j=idx
          while j>0 and n[j]==n[j-1]:
	    j=j-1
	  n[j]=str(int(n[j])-1)
          idx=j 
        idx=idx+1
  idx=0
  while n[idx]=='0':
       idx=idx+1
  print "Case #{}: {}".format(i, "".join(n[idx:]))
