# q13-1.py
# tic tac totem - greendost

def run(inputFileName):
   inputFile = open(inputFileName, "r")
   outputFile = open("output1.txt","w")
   outList = solve(inputFile)
   for x in outList:
      outputFile.write("%s\n" % x)
   inputFile.close()
   outputFile.close()

def solve(inputFile):
   numTc = int(inputFile.readline())
   statList = ['X won','O won','Game has not completed','Draw']  

   outList = []
   for x in range(numTc):
      tc = readTc(inputFile)
      r = evalTc(tc)
      outList.append("Case #" + str(1+x) + ": " + statList[r]) 
      inputFile.readline() 
   
   inputFile.close()
   return outList

def evalTc(tc):
   bRunning = 0 != len([1 for x in range(len(tc)) 
			if(tc[x].find(".") != -1)])
   if bRunning: 
      r = 2
   else:
      r = 3

   for x in range(len(tc)):
      if evalWin(tc[x],"X"):
         r = 0
         break
      if evalWin(tc[x],"O"):
         r = 1
         break
   return r

def evalWin(tc1, char1):
   return 4 == len([1 for x in range(4) if tc1[x] == char1 or tc1[x] == "T"])

def readTc(inputFile):
   ii = []
   r = []
   for x in range(4):
      ii.append(inputFile.readline()[:4])
   for y in range(4):
       r.append(''.join([ii[x][y] for x in range(4)]))
   r.append(''.join([ii[x][x] for x in range(4)]))
   r.append(''.join([ii[x][len(ii[x]) - 1 - x] for x in range(4)]))
   r += ii
   assert 10 == len(r)
   return r

if __name__ == "__main__":
   import sys
   run(sys.argv[1])  
