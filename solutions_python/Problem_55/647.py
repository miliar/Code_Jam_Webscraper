#Kyle Fritz <kyle.p.fritz@gmail.com>
#Code Jam Qualification Round 2010
#problem C

from collections import deque
import sys
    
writeerror=lambda s: sys.stderr.write(s+"\n") 

def coasterCash(rTrips,kCapacity,nGroups,groups):
  q=deque(groups)

  if(not len(q)==nGroups):
    writeerror("fuck: group count doesn't match")
  
  cash=0
  train=[]
  for t in range(rTrips):
    seats=kCapacity
    q.extend(train)#extendright
    train=[]
    while len(q)>0 and seats>=q[0]:
      group=q.popleft()
      seats-=group
      cash+=group
      train.append(group)
    #writeerror("train left %s cash %s"%(train,cash))
  return cash

if __name__=="__main__":
  import sys, csv

  reader = csv.reader(open(sys.argv[1]), delimiter=' ',quoting=csv.QUOTE_NONE)
  getIntList=lambda: map(int,reader.next())
  nCases=getIntList()[0]
  for c in range(nCases):
    rkn=getIntList()#[:2] #ignore N groups
    groups=getIntList()
    cash=coasterCash(*rkn,groups=groups)
    print "Case #%s: %s"%(c+1,cash)

      