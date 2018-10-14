#!/usr/bin/python

import sys

def getDictList(f, D, L) :
   dictList=[]
   for i in range(0, D):
      str = f.readline() 
      dictList.append(str[:L])
   return dictList



def getList (L, str):
   withinParan=0
   outsideParan=1

   tmpList = []
   ML = []
   for i in range(0, L):
      ML.append(tmpList[:])

   mulStr = []
   oneStr = []
   state = outsideParan
   
   count = 0
   tmpList = []
   for ch in str:
      if (ch == '(') :
         state = withinParan
      elif (ch == ')') :
         state = outsideParan
         count = count + 1
      else :
         if state == withinParan:
            ML[count].append(ch)
         else :
            ML[count].append(ch)
            count = count + 1
   return ML


def getPermList(L, mainList):

   permListTuple=[]
   for i in range(0, L):
      permListTuple.append('X')
      
   permList=[]
   for i in range(0,permCount) :
      permList.append(permListTuple[:])

   patternRepeat = 0
   charRepeat    = permCount

   col = 0
   for l in mainList:
      charRepeat = charRepeat / len(l)
      patternRepeat = permCount/ (len(l) * charRepeat)
      row = 0
      for j in range(0, patternRepeat):
         for ch in l :
            for i in range(0, charRepeat) :
               permList[row + i][col] = ch
            row = row + charRepeat

      col = col + 1
  
   permStrList = []
   for i in range(0, permCount) :
      str = "";
      for j in range(0, L) :
          str = str + permList[i][j]
      permStrList.append(str);
      
            
   return permStrList

def getColVal(rowRqd, col, mainList, permCount):

   charRepeat = 0
   charRepeat = permCount
    
   count = 0
   for l in mainList:
      if count <= col :
         count += 1
         charRepeat = charRepeat / len(l)
         patternRepeat = permCount/ (len(l) * charRepeat)
      else :
         break

   row = 0
   for j in range(0, patternRepeat):
      for ch in mainList[col] :
         for i in range(0, charRepeat) :
            if (row + i) == rowRqd :
               return ch
         row = row + charRepeat
  
def getCount(dictList, charList, L):
   count = 0
   for e in dictList:
      found = 1
      for i in range(0, L):
         try :
            charList[i].index(e[i])
         except ValueError :
            found = 0
            break; 
      if found == 1 :
         count+=1
   return count


def testcase(f):
   str = f.readline()
   LDN = str.split()
   L=int(LDN[0])
   D=int(LDN[1])
   N=int(LDN[2])

   dictList = getDictList(f, D, L)

   for i in range(0, N):
      str=f.readline() 
      str=str.replace('\n', "")
      count = 0
      charList = getList(L, str)
      count = getCount(dictList, charList, L)
      print "Case #%d: %d" % (i + 1, count)

def main(arg) :
   f = open(arg, "r")
   testcase(f)

if __name__ == "__main__":
   if len(sys.argv) < 2 :
      print "Usage %s:<Input File name>\n" % sys.argv[0]
   else :
      main(sys.argv[1])
