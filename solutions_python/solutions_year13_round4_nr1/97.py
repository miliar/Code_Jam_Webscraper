import math
import collections

def licz(x, n):
  return -(x**2-x)/2


t = int(raw_input())
for i in range(1, t+1):
  n, m = [int(z) for z in raw_input().split()]
  pairs = []
  pairs1 = []
  suma=0
  for j in range(1, m+1):
    o,e,p = [int(z) for z in raw_input().split()]
    #pairs.append((o,e,p))
    pairs1.append((o,p))
    pairs1.append((e,-p))
    suma+=licz(e-o, n)*p
    
  pairs1=sorted(pairs1, key=lambda x: (x[0], -x[1]))
  #print pairs1
  #print suma
  
  bilety=collections.defaultdict(int)
  for s,p in pairs1:
    if p>0:
      bilety[s]+=p
    else:
      p=-p
      #print list(reversed(bilety.items()))
      for k,v in sorted(reversed(bilety.items()), reverse=True):
        if v==0:
          continue
        mini=min(p,v)

        bilety[k]-=mini
        if bilety[k]==0:
          del bilety[k]
        p-=mini
        suma-=licz(s-k, n)*mini
        if p==0:
          break
  
  #print bilety
  #print 'Case #'+str(i)+': '+str(suma) 
  print 'Case #'+str(i)+': '+str(suma%1000002013)
    