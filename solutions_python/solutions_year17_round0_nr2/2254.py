

import sys
f = open("tat","r")


num=int(f.readline())
case=1

while case<=num:
  line=f.readline().rstrip('\n')
  mst=map(lambda x: int(x),line)
  mlen=len(mst)

  sys.stdout.write("Case #"+str(case)+": ")
 
  #for i in range(len(mst)-1):
  i=0
  while i<len(mst)-1:
    if mst[i]>mst[i+1]:
      mst[i]-=1
      for j in range(i+1,len(mst)):
        mst[j]=9
      i=0
      continue
    i+=1


  fo=False
  for i in range(len(mst)):
    if mst[i]==0 and not fo:
      continue
    else:
      fo=True
      sys.stdout.write(str(mst[i]))
  print("")
  case+=1
