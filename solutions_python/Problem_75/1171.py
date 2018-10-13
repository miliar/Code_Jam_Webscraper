

global lCombs, lOps, lInovke

def createList (sCombs, sOps, sInvoke):
  global lCombs, lOps, lInovke
  
  
  lCombs = {}
  for x in sCombs:
    lCombs[str(x[1]) + str(x[0])] = x[2]
    lCombs[str(x[0]) + str(x[1])] = x[2]
    
  lOps = []  
  for x in sOps:
    t = [x[0], x[1]]
    lOps.append(x)
    
    
  lInovke = sInvoke


def subs (l): 
  global lCombs
  
  ss =  l[ (len(l)-2) :]
  
  
  
  try:
    ss = str(ss[0]) + str(ss[1])
    e = lCombs[str(ss)]
    l = l[: (len(l)-2)]
    l.append(e)
    
  except : pass
  
  return l
  
  
def check(l):
  global lOps

  for sop in lOps:

    if sop[0] in l and  sop[1] in l: 
	return True
  return False
  
  
def main ():
  global lInovke
  l = []
  
  for x in lInovke:
    
    l.append(x)
    l = subs(l)
    if check(l): l = []
    
  return l
  
  

#

import sys,re 

def readFileandExe(filename):
  global lCombs, lOps, lInovke
  
  f  = open(filename)
  fo = open(filename+".o", 'w')
  N = int(f.readline())
  
  for j in range(N):
    ST  = str(f.readline()) 
    ST = ST.split()
    print ST
    
    
    i = 1
    
    sComb = []
    while not re.search('[0-9]', ST[i]):
      sComb.append(ST[i]);  i +=1
    i +=1
    sOps = []
    while not re.search('[0-9]', ST[i]):
      sOps.append(ST[i]);  i +=1
    i +=1  
    sInvoke = ST[i]  

    #print sComb
    #print sOps
    #print sInvoke
    
    createList(sComb, sOps, sInvoke)
    res = main()
    print res

    if res == []:
      fo.write ("Case #" + str(j+1) +': []\n')
    else: 
      st = ''
      for x in res:  st += str(x) + ', '
      fo.write ("Case #" + str(j+1) +": [" + st[:len(st)-2] + ']\n')
    
    
    
  fo.close()
    
  
readFileandExe(sys.argv[1])    
    
    
    
    
    
    
    