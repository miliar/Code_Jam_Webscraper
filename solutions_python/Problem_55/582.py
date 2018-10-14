f=open("/tmp/C-small-attempt1.in",'r')
o=open("out.txt",'w')
T=int(f.readline())
for t in range(T):
  l = f.readline().rsplit()
  R=int(l[0])
  k=int(l[1])
  N=int(l[2])

 
  Q = [int(x) for x in f.readline().rsplit()]
  
  ans = 0
  
  for i in range(R):
    l=[]
    sum = 0
    while sum <= k and len(Q)>0:
      x = Q.pop(0)
      sum = sum + x
      l.append(x)
    if  sum > k:
      sum = sum - x
    ans = ans + sum
    Q.insert(0,l.pop())
    while len(l) > 0:
      Q.append(l.pop(0))
  
  o.write("Case #%d: %d\n" %(t+1,ans))
