import bisect




#def checkTidy()
def checkTidy(Number) :
  listNum = list(str(Number))
  print('listNum : ',listNum)
  listNum = list(map(int, listNum))  
  print('listNum : ',listNum) 
  for i in range(1,len(listNum)):
    print(listNum[i],listNum[i-1])  
    if (listNum[i]<listNum[i-1]) :      
      return 0
    #return true
  return 1
  
resultText =''
countLine = 0
#with open('exB.in','r') as ifile, open('plaBex.out','w') as ofile, open('debug.out','w') as oDfile, open('dataRcheck.out','w') as oRfile:
with open('B-small-attempt0.in','r') as ifile, open('plaSmall.out','w') as ofile, open('debug.out','w') as oDfile, open('dataRcheck.out','w') as oRfile:
  
  for line in ifile :
    print (line)
    #print("6666666666666666666666666666666666666666666666666")
    if countLine == 0 :
      case = line.split()
      case = int(case[0])
      print ("case : ",case)
    else : 
      Number = line.split()
      print('Number : ',Number)
      Number = int(Number[0])
      print('Number : ',Number)
      #for i in listNum :
      #count = 0
      while((checkTidy(Number)==0)):      
      #while((checkTidy(Number)==0)):
        #count = count +1 
        Number = Number - 1
        print('Number : ',Number)
      print ('out of while loop now')      
      resultText = 'Case #'+str(countLine)+': '+str(Number)+'\n' 
      ofile.write(resultText)
      
    countLine = countLine + 1
    