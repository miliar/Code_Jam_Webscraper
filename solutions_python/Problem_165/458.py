import filecmp
import numpy as np
import operator
import itertools


def printDebug(text, value) :
  debLine = text+str(value)+'\n'
  print("  ",debLine)
  oDfile.write(debLine)

def slove(R,C,S):
  if S == 1 :
    return R*C
  elif S == C and R == 1:
    return C
    printDebug("111 treeL : ",treeL)
  else :
    HS = S / 2
    R = C / S
    HC = C / 2
    RM = C % S
    printDebug("C : ",C)
    printDebug("S : ",S)
    hit = 0
    if RM == 0 :
      while C >= S :
        C = C - S
        hit = hit + 1
        printDebug("hit : ",hit)
      hit = hit + (S-1)
      printDebug("hit * * : ",hit)
      return hit
    elif RM > 0 :
      while C >= S :
        C = C - S
        hit = hit + 1
        printDebug("hit : ",hit)
      hit = hit + (S)
      printDebug("hit -- : ",hit)
      return hit
    else :
      printDebug("sfjl : ",00)	 

  '''
  N&C = []
  carry = [0,0]
  node = set(itertools.chain.form_iterable(treeL))
  nodeL = list(itertools.chain.form_iterable(treeL)) 
  for i in range (len(node)) :
    carry[1] = i
    carry[2] = nodeL.count(node[i])
    n&C.append(carry)
  for j in range (N&C) : 
        
    if N&C[j][2] != 0 or N&C[j][2] != 2 :
      break
    elif (N&C[j][2] != 0 or N&C[j][2] != 2) and j == (len(N&C)) :
      return 0
    N&C[j][2]   
  '''
  return 0;

outLine = ''
countLine = 0
countCase = 0
first = 0
second = 0
N = 0
treeL=[]
#A-small-practice.txt
#A-EX.in
#A-EX-PLA.out
with open('A-small-attempt0.in','r') as ifile, open('A-pla.out','w') as ofile, open('A-BUG.out','w') as oDfile :
#with open('A-EX.in','r') as ifile, open('A-EX-pla.out','w') as ofile, open('A-EX-BUG.out','w') as oDfile :
  for line in ifile : 
    printDebug("line : ",line)
    
    if countLine == 0 : 
      case = line.split()
      case = int(case[0])
      printDebug("case : ", case)
      #case = int(line.split())
      #printDebug("",0)
    else : 
      R,C,S = list(map(int,line.split()))   
      sol = slove(R,C,S)
      outLine = 'Case #'+str(countCase+1)+': '+str(sol)+'\n'
      print(outLine)
      printDebug("**************************countCase*********    ",countCase+1)      
      ofile.write(outLine)
      countCase = countCase + 1
          
    
    '''
    elif countLine > 0 and N == 0:
      N = line.split()
      N = int(N[0])
      printDebug("N : ", N)
    elif countLine > 0 and N > 0:
      ML =list(map(int,line.split()))
      treeL.append(ML)
      N -= N
      printDebug("treeL : ", treeL)
      if N <= 0 :
        sol = slove(treeL)            
        outLine = 'Case #'+str(countCase+1)+': '+str(sol)
        print(outLine)
        printDebug("**************************countCase*********    ",countCase+1)      
        ofile.write(outLine)
        countCase = countCase + 1
      #printDebug("within calculation---------------------------------------------------------------------------------------",0) 
  
    else :
      printDebug("IMPOSSITLBE : ",44)
    '''  
    
    if countCase == case :
      print("break")
      break
    countLine = countLine + 1
   


#'''
ifile.close()
ofile.close()
oDfile.close()
#oRfile.close()
#'''
'''
import cProfile 

from pympler import tracker
tr = tracker.SummaryTracker()

pr=cProfile.Profile()
pr.enable()
'''
'''
ifile.close()
ofile.close()
debFile.close()
pr.disable()
pr.print_stats(sort='time')
tr.print_diff()
'''
