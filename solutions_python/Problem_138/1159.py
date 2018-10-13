#Graham Erickson

import copy

def naomiPlayer(naomi,ken):
  covered=True
  curMax=1.0

  
  minNaomi=naomi[-1]
  minKen=ken[-1]
  maxKen=ken[0]
  maxNaomi=naomi[0]

  for i in range(len(naomi)):
    if naomi[i] < ken[i]:
      covered=False
    
  if covered:
    return (maxKen+0.000001,minNaomi)
  else:
    return (maxKen-0.000001, minNaomi)

def playDeceitfulWar(n,naomi,ken):
  nPoints=0
 
  naomi.sort()
  ken.sort()
  naomi.reverse()
  ken.reverse()
  
  for i in range(n):
    #print naomi, ken
    told,chosen = naomiPlayer(naomi,ken)
    naomi.remove(chosen)
    kChosen = kenPlayer(told,ken)
    #print "y ", told, chosen, kChosen
    #print naomi, ken
    if chosen>kChosen:
      nPoints+=1
  return nPoints


def playNormWar(n,naomi,kenBlocks):
  nPoints=0
  for i in range(n):
    naomiBlock=naomi[i]
    kChosen = kenPlayer(naomiBlock,kenBlocks)
    if naomiBlock>kChosen:
      nPoints+=1
  return nPoints

def kenPlayer(nTold,kenBlocks):
  # selects and removes one of kens blocks based on what naomi says
  canBeat=False
  minDis=1.1
  minBlock=None

  smallBlock=1.1
  for x in kenBlocks:
    if x>nTold:
      canBeat=True
    if canBeat and (x-nTold)>0 and (x-nTold)<minDis:
      minDis=x-nTold
      minBlock=x
    if not canBeat:
      if x<smallBlock:
        smallBlock=x

  chosenBlock=0.0
  if canBeat:
    chosenBlock=minBlock
  else:
    chosenBlock=smallBlock
  kenBlocks.remove(chosenBlock)
  return chosenBlock

def main():
  f=open("D-large.in",'r')
  lines=f.readlines()
  lines=lines[1:]
  i=0
  casen=1
  while i <len(lines):
    n=int(lines[i].strip("\n"))
    naomi=map(lambda x:float(x),(lines[i+1].strip("\n")).split())
    ken=map(lambda x:float(x),(lines[i+2].strip("\n")).split())
    ken2=copy.copy(ken)
    naomi2=copy.copy(naomi)
    nw = playNormWar(n,naomi,ken)
    dw = playDeceitfulWar(n,naomi2,ken2)

    print "Case #"+str(casen)+": "+str(dw)+" "+str(nw)
    casen+=1
    i=i+3

  #print playDeceitfulWar(3,[0.5,0.1,0.9],[0.6,0.4,0.3])

if __name__=='__main__':
  main()





