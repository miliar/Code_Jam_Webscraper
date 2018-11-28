# -*- coding: utf-8 -*-
def check(x,y,ori):
  #print ori
  #print x,y
  if x>=(len(ori)-1):
    return 0
  if y>=(len(ori[0])-1):
    return 0
  
  if ori[x][y]=='#' and ori[x+1][y]=='#' and ori[x][y+1]=='#' and ori[x+1][y+1]=='#':
    ori[x][y]="/"
    ori[x+1][y]="\\"
    ori[x][y+1]="\\" 
    ori[x+1][y+1]="/"
    return 1;
  return 0

def ans(line):
  #num = int(line.strip())
  #line = sys.stdin.readline()    
  sLine= line.strip().split()
  X = int(sLine[0])
  Y = int(sLine[1])
  ret =[];
  ori=[];
  x=0;
  y=0
  for i in range(X):
    line = sys.stdin.readline()    
    #retT =[]
    oriT= []
    for c in line.strip():
      oriT.append(c);
    ori.append(oriT)
  #print ori
  
  for i in range(X):
    for j in range(Y):      
      if ori[i][j]=='#':
  	if not check(i,j,ori):
	  print 'Impossible'
	  return
  
  for line in ori:
    s =""
    for c in line:
      s+=c;
    print s
  
  
  
  

if __name__=="__main__":
  import sys
  line=sys.stdin.readline()
  M=int(line.strip())
  for caseI in range(1,M+1):
    print "Case #"+str(caseI)+": "
    ans(sys.stdin.readline());
    #line=sys.stdin.readline()
    