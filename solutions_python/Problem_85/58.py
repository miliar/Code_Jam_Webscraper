# -*- coding: utf-8 -*-


def ans(line):
  #num = int(line.strip())
  #line = sys.stdin.readline()    
  sLine= line.strip().split()
  L = int(sLine[0])
  t = int(sLine[1])
  N = int(sLine[2])
  C = int(sLine[3])
  ai = []
  sumA =0;
  for i in range(4,C+4):
    ai.append(int(sLine[i]))
    sumA+=ai[i-4];
  #print 'L:',L,'t:',t,'N:',N,'C:',C
  #print 'ai:',ai
  #print 'sumA:',sumA
  comp = (t/2)/sumA;  
  extra = (t/2)%sumA
  #print 'extra:',extra
  #print 'comp:',comp
  starR = comp*C
  #print 'starR',starR
  morSR = 0;
  remain = 0;
  if extra>0:
    for i in range(0,C):
      #print i,ai[i]
      if extra ==0:
	break
      if extra >= ai[i]:
	extra -= ai[i];
	morSR+=1
      else:
	remain = ai[i]-extra 
	morSR+=1
	break
  
  if (starR+morSR)>N:
    tr = N/C
    totalSum = tr*sumA;
    tS =N%C;
    for i in range(tS):
      totalSum+=ai[i]
    return totalSum*2    
    #return
  
  for i in range(morSR):
    temp = ai[0]
    del ai[0]
    ai.append(temp);
  #print 'new ai',ai
  starR+=morSR;
  #print 'starR',starR
  #print 'remain',remain
  dic={}
  lis=[]
  if remain>0:
    dic[remain]=0
    lis.append([remain,1])
    
  
  
  
  nR = N-starR;
  tot = nR/C;
  #print 'nR1:',nR,'  tot:',tot
  for i in range(C):
    if ai[i] in dic:
      ind = dic[ai[i]];
      lis[ind][1]+=tot
    else:
      dic[ai[i]]=len(lis)
      lis.append([ai[i],tot])
  nR = nR%C
  for i in range(nR):
    if ai[i] in dic:
      ind = dic[ai[i]];
      lis[ind][1]+=1
    else:
      dic[ai[i]]=len(lis)
      lis.append([ai[i],1])
  #print 'dic:',dic
  #print 'lis'
  #for i in lis:
    #print i
 
  lis.sort(key = lambda x:-x[0])
  #print 'sorted lis'
  #for i in lis:
    #print i
  
  tL = L;
  retVal = t;
  #print 'L:',L
  #print 'C:',C
  #print 'ai',ai  
  #print 'lis before'
  #for i in lis:
    #print i
  while tL >0 and len(lis)>0 :
    temp = lis[0];
    if tL>=temp[1]:
      tL-=temp[1]
      retVal+=temp[0]*temp[1];
      del lis[0]
    else:
      lis[0][1]-= tL
      retVal+=temp[0]*tL;
      tL =0;
  for t in lis:
    retVal+=2*t[0]*t[1];
  #print 'lis after'
  #for i in lis:
    #print i  
  return retVal
  

if __name__=="__main__":
  import sys
  line=sys.stdin.readline()
  M=int(line.strip())
  for caseI in range(1,M+1):
    print "Case #"+str(caseI)+": ",ans(sys.stdin.readline());
    #line=sys.stdin.readline()
    