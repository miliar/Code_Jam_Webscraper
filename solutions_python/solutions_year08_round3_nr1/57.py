inf=100000000

import math
import string
import decimal
  
# inizio corpo

f=open("input.txt","r")
o=open("output.txt","w")

numcasi=int(f.readline())

i=1
while i<=numcasi:
  s=f.readline()
  m=string.split(s)
  P=long(m[0])
  K=long(m[1])
  L=long(m[2])
  s=f.readline()
  m=string.split(s)
  freq=[]
  for elem in m:
    freq.append(long(elem))
  freq.sort()
  freq.reverse()
  print freq
  if P*K<L:
    o.write("Case #%d: Impossible\n" % (i))
    break
  somma=0
  it=0
  molt=1
  while it<len(freq):
    cont=0
    while cont<K and it<len(freq):
      somma+=molt*freq[it]
      cont+=1
      it+=1
    molt+=1
  o.write("Case #%d: %d\n" % (i,somma))
  i=i+1
f.close()
o.close()
