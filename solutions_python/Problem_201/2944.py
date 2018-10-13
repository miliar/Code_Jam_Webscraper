import bisect


def odd (R):
  Rlist = []
  #print(int(R/2),'odd')
  bisect.insort(Rlist,int(R/2))
  bisect.insort(Rlist,int(R/2))  
  #print("odd ",Rlist)
  return Rlist
def even (R):
  Rlist = []
  #print(int(R/2),'even')
  bisect.insort(Rlist,int(R/2))
  bisect.insort(Rlist,int(R/2)-1)
  #print("even ",Rlist)
  return Rlist
  
def solution (R,P) :
  Rlist=[]
  #print(R%2)
  #print(int(R/2),'[[[[[',P)
  cList=[]
  for i in range(1,P+1,1) :
    #print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',i)
    if i == 1 :
      if (N%2 == 1) :
        Rlist = odd(N)
      else :
        Rlist = even(N)
    else :
      
      Ms = Rlist[-1]
      if (Ms%2 == 1) :
        #print(Rlist,"odd")
        cList = odd(Ms)
        bisect.insort(Rlist,cList[0])
        bisect.insort(Rlist,cList[1])
        Rlist.pop()
        #print(Rlist,"even")
      else :
        #print(Rlist,"==")
        cList = even(Ms)
        bisect.insort(Rlist,cList[0])
        bisect.insort(Rlist,cList[1])        
        Rlist.pop()
        #print(Rlist,"00000000000000000000000000000")
    #print("Rlist Rlist last",Rlist)
  #print('-----------cList',cList)
  return cList

  
resultText =''
countLine = 0
with open('C-small-1-attempt2.in','r') as ifile, open('platry2.out','w') as ofile, open('debug.out','w') as oDfile, open('dataRcheck.out','w') as oRfile:
#715 679  
#with open('exC.in','r') as ifile, open('plaCex.out','w') as ofile, open('debug.out','w') as oDfile, open('dataRcheck.out','w') as oRfile:
  for line in ifile :
    #print (line)
    #print("6666666666666666666666666666666666666666666666666")
    #print('skfjlfksjflakjsdkljfds')
    #print('skfjlfksjflakjsdkljfds')
    '''
    if (countLine == 97):
      print('skfjlfksjflakjsdkljfds')    
    '''
    if countLine == 0 :
      case = line.split()
      case = int(case[0])
      print ("case : ",case)
    else : 
      N,K = list(map(int,line.split())) 
      if (countLine == 97):
        print("skjfdklsj",N,K)
      if (N == 1) and (K==1) :
        resultText = 'Case #'+str(countLine)+': 0 0\n'  
        ofile.write(resultText)       
      else :
        if N == K :
          x = 0
          y = 0
          resultText = 'Case #'+str(countLine)+': 0 0\n'  
          ofile.write(resultText)
          if (countLine == 97):
            print('----------------skfjlfksjflakjsdkljfds')         
          #print("outLine : ",resultText)        
        if K == 1 :
          if (N%2 == 1) :
            Rlist = odd(N)
          else :
            Rlist = even(N)
          #print(R%2)
          #Rlist = even(N)
          resultText = 'Case #'+str(countLine)+': '+str(int(Rlist[1]))+' '+str(int(Rlist[0]))+'\n'  
          ofile.write(resultText)
          if (countLine == 97):
            print('---skfjlfksjflakjsdkljfds')         
          #print("outLine : ",resultText)
        if (N != K) and (K != 1) :
          #print('other')
          cList = solution(N,K)
          resultText = 'Case #'+str(countLine)+': '+str(int(cList[1]))+' '+str(int(cList[0]))+'\n'  
          ofile.write(resultText)  
          if (countLine == 97):
            print('skfjlfksjflakjsdkljfds---')         
          #print('other')   
      
    countLine = countLine + 1
    