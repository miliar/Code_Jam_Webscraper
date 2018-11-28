import filecmp
import numpy as np
import cProfile 
import math
from pympler import tracker
tr = tracker.SummaryTracker()

pr=cProfile.Profile()
pr.enable()


def printDebug(text, value) :
  debLine = text+str(value)+'\n'
  print("  ",debLine)
  oDfile.write(debLine)
	



countLine=0
countCase=0
noFoodOption=0
currentFoodOption=0
newResol = 0
resultText = ''
output =''
result = 0
#test = [[0 for col in range(1,4)] for row in range(1,4)]
'''
if len(result) == 0:
  resultText = 'Case #'+str(countCase)+': '+'no\n'
else :
  resultText = 'Case #'+str(countCase)+': '+'yes\n'
  ofile.write(resultText)
'''
'''	
def handle_fitting(X, C, R) :
  result = 0
 
  if (C%2) == 1 or (R%2) == 1 :
    #
    
  if((X%2)==0) :
    #even 2 4  
    if R<X and C<X:
    #sure
      result = 1
  else :
    #odd 1 3
    
  return result
'''
'''
      if ((X%2) == 0) :
        Mod = S/X
        Q = make_list(T)
        #printDebug("test : ",test)
'''
'''
	  if R
	  elif C :
	else :
	#odd 1 3
'''
'''
  if max == 1 :
    result = 1
  if max == 2 :
    result = 2
  if 4 >= max >= 3 or  max == 6 or max == 8:
    result = 3
  if max == 7 or max == 9 or max == 5:
    result = 4
  return result
'''
'''
math.ceil(5/2)
''' 

def make_list(T) :
  for i in range (0,4) :
    printDebug("II : ",i)
    for j in range (0,4) :
      printDebug("j : ",j)
      printDebug("i : ",i)
      k = (j+1)*(i+1)
      T[i][j] = k
    printDebug("T : ",T)
    #OT.append(T)
    printDebug("OT : ",OT)
    
  return OT

'''
        if (S%X) == 0 :
	  result = 1
	  #handle_fitting(X, C, R)
        else :
	  #space or ove
	  result = 0 
	  #Richar
'''
def pla(S,X) :
  if (S%X) == 0 :
    result = 1
    #handle_fitting(X, C, R)
  else :
    #space or ove
    result = 0 
    #Richard
  return result
OT = []
T = []
#carry[5] = []
#'B-small-attempt1.in'
#'B-EX.in'
T = [[0 for col in range(1,5)] for row in range(1,5)]
#D-small-attempt0.in
#'D-EX.in'
#'D-small-attempt0.in'
with open('D-small-attempt1.in','r') as ifile, open('Doutput.out','w') as ofile, open('Ddebug.out','w') as oDfile, open('DdataRcheck.out','w') as oRfile:
#with open('D-EX.in','r') as ifile, open('D-EX-output.out','w') as ofile, open('DEXdebug.out','w') as oDfile, open('DdataRcheck.out','w') as oRfile:
  for line in ifile :	
    print (line)
    if countLine == 0 :
      case = int(line)
      printDebug('case', case) 
    elif countLine > 0:
      
      [X, R, C] = map(int,line.split())
      printDebug(" X : ",X)
      printDebug(" R : ",R)
      printDebug(" C : ",C)
      S = R * C
      print(" S : ",S)
      #st1 = S%X
      if X == 1 : 
        result = 1
        printDebug("X == 1 : ",X == 1)
      if X > S :
        result = 0
      elif X == 2 and ((S%2)!= 0) :
        result = 0
        printDebug("2 : ",2)
      elif X == 3 and ((S%3)!= 0) :
        result = 0
        printDebug("3 : ",3)	
      elif X == 4 and ((S%4)!= 0) :
        result = 0	
        printDebug("4 : ",4)		
        printDebug("4  2  : ",42)
      elif ((X == 4) and ((S%4)== 0)) and ((C <= 2 or R <= 2)) :
        result = 0	
        printDebug("4  2  : ",42)
      elif (C == 1 or R == 1) and ((X >=3)):
        #if((math.ceil(X/2))>=C) or ((math.ceil(X/2))>=R) 
        # C or R < #(X >=3)
        result = 0
        printDebug("444 : ",444)	
      else :
        result = pla(S,X)
        printDebug("pla : ",result)
	
      print("000000000000000000",result)
      countCase = countCase + 1
      #resultText = 'Case #'+str(countCase)+': '+str(result)+'\n'
      if result == 0 :
        resultText = 'Case #'+str(countCase)+': '+'RICHARD'+'\n'
      if result == 1 :
        resultText = 'Case #'+str(countCase)+': '+'GABRIEL'+'\n' 
      printDebug("resultText : ",resultText)
      ofile.write(resultText)	
    #resultText = 'Case #'+str(countCase)+': '+'yes\n'
    '''
      if st1 == 0 :
        R
        C
        handle_fit()
    '''
    '''
    elif (countLine % 2) == 1:
      P = int(line)
      printDebug('P : ', P) 
    elif (countLine % 2) == 0:	
      PD = list(map(int,line.split()))
      printDebug('before PD : ', PD)
      PD2 = sorted(PD, reverse=True)
      printDebug('sorted PD : ', PD2)
      result = solution(PD2[0])
      countCase = countCase + 1

      ofile.write(resultText)
    '''
    
    if countCase == case : 
      print("break")
      break
    countLine += 1
    #test = [[0 for col in range(0,4)] for row in range(0,4)]
    #printDebug("test : ", make_list(T))
'''
if filecmp.cmp('Doutput.out','D-Ominous.out',shallow=False):
	print ('pass test')	
''' 	
ifile.close()
ofile.close()
oDfile.close()
oRfile.close()
pr.disable()
pr.print_stats(sort='time')
tr.print_diff()
#tr.print_diff()
#objgraph.show_most_common_types()
#print (objgraph.show_most_common_types())
'''
x = h.heap()
print (h.heap())
print (x.size)
print (h.iso(result).domisize)
#not working with python 3
'''
