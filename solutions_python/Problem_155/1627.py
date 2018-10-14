
   
#'''
def amount_people(PP) :
  result = 0
  cResult = 0
  PPR = PP[::-1]
  PPR = list(map(int,PPR))
  #printDebug("PPR : ",PPR)
  M2 = len(PP) - 1
  #printDebug("M2 : ",M2)
  for i in range (len(PP)-1) :
    #PPR[i]
    #printDebug("len of less lev",len(PPR[i+1::]))
    lev = len(PPR[i+1::])
    SPPI = sum(PPR[i+1::])
    carry = SPPI-lev
    #if i > 0 :
    if carry > 0 and i == 0:
    #no need
      carry = 0
    elif carry <= 0 and i == 0:
      result = abs(carry)
      
    if i > 0 and carry < 0 and abs(carry) > result  :
      result = abs(carry)
  return result

Padd = 0
countLine=0
countCase = 0 
result = 0
#example.in
#D-small-practice.in
#'A-EX.in'
#'A-small-attempt0.in'
with open('A-large.in','r') as ifile, open('output.out','w') as ofile, open('debug.out','w') as oDfile, open('dataRcheck.out','w') as oRfile:
  for line in ifile :
    #print (line)
    if countLine == 0 :
      case = line.split()
      case = int(case[0])
      #case = int(line.split())
    elif countLine >= 1 and countCase >= 0 and countCase <= case :
      [M, PP] = map(str, line.split())
      M = int(M)
      PP = str(PP)
      PP = iter(PP)
      PP = ' '.join(PP)
      PP = PP.split()
      result = amount_people(PP)
      countCase = countCase + 1
      outLine = 'Case #'+str(countCase)+': '+str(result)+'\n'
      ofile.write(outLine)
    else :
      printDebug("IMPORSIBLE ??!!",99)
    if countCase == case : 
      #print("break")
      break
    countLine = countLine + 1

ifile.close()
ofile.close()
oDfile.close()
oRfile.close()


