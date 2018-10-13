
t=int(raw_input())
j=1
h=[]
while j<=t:
  s=raw_input()
  n=int(s)
  if len(s) == 1:
    print "Case #%d: %d"%(j,n)
  else:
   for i in range(n,0,-1):
    m = list(str(i))
    if all(m[k] <= m[k+1] for k in xrange(len(m)-1)):
      #print b
      #print m
      print "Case #%d:"%(j),"".join(m)
      break
    else:
      continue
  j+=1

