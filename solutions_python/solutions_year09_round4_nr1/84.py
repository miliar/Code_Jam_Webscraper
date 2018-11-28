# -*- coding: utf-8 -*-

def getRank(l):
  for i in range(len(l)-1,-1,-1):
    if l[i]=='1':
      return i;
  return 0
  
  
def check(rank,lL): 
  print "\n\n\n"
  print rank
  for i in lL:
    print i 
  #maxI=-l-1
  minI=len(lL)+1
  for i in range(len(rank)):
    if (rank[i]) > i:
      minI=i
      break
    #if rank[i] < i and maxI<i:
      #maxI=i
  if minI==len(lL)+1:
    return 0,[],0
  count=0
  chg=len(lL)
  for i in range(minI+1,len(rank)):
    if (rank[i])<=minI:
      chg=i;
      break;
  count=chg-minI
  print chg
  del lL[chg]
  tempL=lL[minI:]
  newT=[]
  for i in tempL:
    newT.append(i[minI+1:]) 
  print "  count:",count,"  minI:",minI,"  chg:",chg
  return 1,newT,count

      
  
  
if __name__=="__main__":
  #global N,M
  #fd=open("A-large-practice.in","r")
  fd=open("A-large.in","r")
  #fd=open("input","r")
  caseNum=int(fd.readline().strip())
  print "numis ",caseNum
  fw=open("outputLarge","w")
  #l=[1,2,3,4]
  
  #while -1 not in l:
    #print l
    #l=getNext(l)
    
  
  
  for caseI in range(caseNum):
    fw.write("Case #"+str(caseI+1)+": ")
    line=fd.readline().strip()
    num=int(line)
    listL=[]
    
    #l=list(str(num))
    for i in range(num):
      line=fd.readline().strip()
      listL.append(line)
    rank=[]
    finalL=[]
    print "\n\n\nfor "+str(caseI+1)
    for i in listL:
      print i
      #listL=check(rank,listL)
      #if rank[i]!=(i):
	#finalL.append(i)
    print rank
    count=0
    #1,newT,count
    length=len(rank)-1
    while 1:
      rank=[]
      for i in range(len(listL)):
	rank.append(getRank(listL[i]))
      flag,listLTemp,tmpC=check(rank,listL)
      count+=tmpC
      #print flag
      if flag==0:
	break
      listL=listLTemp
    fw.write(str(count)+"\n")
    print count
    