import sys
import re
import os

def freecell():
  
  N = int(next(fin).strip())
  
  gamelst = []
  wplst = []
  owplst = []
  
  for x in range(N):
    gamelst_ = []
    gamelst_ = list(next(fin).strip())
    wp = float()
    win = gamelst_.count('1')
    loss = gamelst_.count('0')
    
    wp = float(float(win)/(win +loss))
    
    owplst_ = []
    val = 0
    wplst.append(wp)
    for y in range(N):
      if gamelst_[y] == '.':
        val = wp  
      if gamelst_[y] == '0':
        val = float(float(win)/(win + loss -1))
      if gamelst_[y] == '1':
        val = float(float(win - 1)/(win + loss -1))
      owplst_.append(val)
    owplst.append(owplst_)
    gamelst.append(gamelst_)  
  
  wpmremlst = []
  wpmremlst.extend(owplst)
  
#  print owplst, wpmremlst
  owplst = []
  for x in range(N):
    opp = 0
    owp = float(0)
    gamelst_ = gamelst[x]
    for y in range(len(gamelst_)):
      if gamelst_[y] == '1' or gamelst_[y] == '0':
        
        owp = owp + float(wpmremlst[y][x])
        opp = opp + 1
    owp = float(owp)/opp
    owplst.append(owp)  
  print owplst   
    
  
  oowplst = []  
  for x in range(N):
    gamelst_ = gamelst[x]
    opp = 0
    owp = float(0)
    for y in range(len(gamelst_)):
      if gamelst_[y] == '1' or gamelst_[y] == '0':
        owp = owp + owplst[y]
        opp = opp + 1
    oowp = float(owp)/opp
    oowplst.append(oowp)
    
    print>>fout, float(0.25 * wplst[x]) + float(0.5 * owplst[x]) + float (0.25 * oowplst[x])
  
  print oowplst
  #  print>>fout, total
    

    
    
if len(sys.argv) != 2:
  print 'specify input file'
  exit()


fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out','w')

numCases = int(next(fin))
for caseNo in range(numCases):
  print>>fout, 'Case #%s:'%(caseNo+1)
  freecell()

fin.close()
fout.close()


  
  

