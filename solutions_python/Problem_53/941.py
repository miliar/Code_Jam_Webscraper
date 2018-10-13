import sys
f=open(sys.argv[1]);
T=int(f.next())


for t in range(T):
  line=f.next()
  l=line.split()
  N=int(l[0])
  K=int(l[1])
  onoff=[]
  power=[]
  for i in range(N):
    onoff.append(False);
    power.append(False);

  power[0]=True
  for i in range(K):
    for j in range(N):
      if power[j]:
	onoff[j]=not onoff[j]
    for j in range(N):
      if onoff[j]==True:
	for k in range(j, N):
	  if power[k]:
	    powered=True
	    for m in range(k+1, N):
	      if onoff[m] and powered:
		power[m]=True
	      elif powered:
		power[m]=True
		powered=False
	      else:
		power[m]=False
		powered=False
      else:
	for k in range(j+1, N):
	  if power[k]:
	    power[k]=False
  toggle="OFF"
  if power[N-1] and onoff[N-1]:
    toggle="ON"
  print "Case #"+str(t+1)+": "+toggle