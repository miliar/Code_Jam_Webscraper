def calcWarScore(nbl,kbl):
  def kMove(kbl,nsd):
    kbl.sort()
    for i in kbl:
      if i>nsd:
        return i
    return kbl[0]

  def nMove(nbl):
    nbl.sort()
    return nbl[-1]
 
  score = 0
  while len(nbl)>0:
    nmv = nMove(nbl)
    kmv = kMove(kbl,nmv)
    kbl.remove(kmv)
    nbl.remove(nmv)
    if nmv>kmv:
      score+=1
  return score


def calcDecScore(nbl,kbl):
  def kMove(kbl,nsd):
    kbl.sort()
    for i in kbl:
      if i>nsd:
        return i
    return kbl[0]

  def nMove(nbl,kbl):
    nsn = 0
    while (nsn<len(nbl)):
      if nbl[nsn]>kbl[0]:
        break
      nsn+=1
    if nsn==len(nbl):
      return (nbl[0],nbl[0])
    return (nbl[nsn],kbl[-1]+ (1-kbl[-1])*nbl[nsn])


  score = 0
  while len(nbl)>0:
#    print nbl
#    print kbl
    nmv = nMove(nbl,kbl)
    kmv = kMove(kbl,nmv[1])
#    print nmv
#    print kmv
#    print

    kbl.remove(kmv)
    nbl.remove(nmv[0])
    if (nmv[0]>kmv):
      score +=1
  return score


 

T = int(raw_input())
for t in range(1,T+1):
  print "Case #"+str(t)+":",
  N = int(raw_input())
  nbl = map(float,raw_input().split())
  kbl = map(float,raw_input().split())
  nbl.sort()
  kbl.sort()
  print calcDecScore(nbl[:],kbl[:]),
  print calcWarScore(nbl[:],kbl[:])

