import itertools

def allSplits(elements,n):
  if n==1:
    return [[elements]]
  c = itertools.combinations(elements,1)
  k = []
  for i in range (1,len(elements)-n+2):
    c = map(set,itertools.combinations(elements,i))
    for i in c:
      for l in allSplits(elements.difference(i),n-1):
        k.append([i]+l)
  return k

def makeTrie(elements):
  tr = set()
  for i in elements:
    for j in range(len(i)+1):
      tr.add(i[:j])
  return tr
  
T = int(raw_input())
for t in range(1,T+1):
  M,N = map(int,raw_input().split())
  S = [raw_input() for i in range(M)]
  allS = {}
  for i in allSplits(set(S),N):
    
    nn = 0
    for j in range(N):
      tr = makeTrie(i[j])
      nn += len(tr)
 
    if nn not in allS:
      allS[nn] = 1
    else:
      allS[nn] +=1
  wst = (0,0)
  for i in [(i,allS[i]) for i in allS]:
    if i[0]>wst[0]:
      wst = i
  print "Case #"+str(t)+": "+str(wst[0])+' '+str(wst[1]%1000000007)
