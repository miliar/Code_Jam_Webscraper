

import sys
f = open("pan1","r")


num=int(f.readline())
case=1

while case<=num:
  line=f.readline()
  (string, size) = line.split()
  size=int(size)
  mst=map(lambda x: x=='+',string)
  #print mst
  mlen=len(mst)

  sys.stdout.write("Case #"+str(case)+": ")
  count=0
  for i in range(len(mst)):
    if mst[i]:
      continue
    if i+size>mlen:
      count=-1
      break
    for j in range(i,i+size):
      mst[j]= not mst[j]
    count+=1
  if count==-1:
    print("IMPOSSIBLE")
  else:
    print(str(count))
  case+=1
