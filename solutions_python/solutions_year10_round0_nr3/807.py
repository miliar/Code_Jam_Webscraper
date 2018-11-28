import sys
f=open(sys.argv[1]);
T=int(f.next())


for t in range(T):
  line=f.next()
  l=line.split()
  R=int(l[0])
  k=int(l[1])
  N=int(l[2])
  
  rollerqueue=[]

  line=f.next()
  l=line.split()

  for g in range(N):
    rollerqueue.append(int(l[g]))
  
  newqueue=[]
  euro=0
  for x in range(R):
    i=0
    while i<=k:
      if i+rollerqueue[0]>k:
	break
      else:
	i+=rollerqueue[0]
	newqueue.append(rollerqueue[0])
	del rollerqueue[0]
	if len(rollerqueue)==0:
	  break
    euro+=i
    for i in newqueue:
      rollerqueue.append(i)
    newqueue=[]
  print "Case #"+str(t+1)+": "+str(euro)