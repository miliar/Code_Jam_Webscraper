#Author: Stefan
class CodeJam:
  def __init__(self,text):
    self.text = text
    self.ref = 'welcome to code jam'
    self.count = 0

  def getCount(self):
    return self.count

  def findNextLetter(self,letter,theString,index):
    for i in range(index,len(theString)):
      if theString[i]==letter:
        return i
    return -1

  def computeNum(self,ref,index):
    if len(ref) == 0:
      return 1
    elif index >= len(self.text):
      return 0
    else:
      counter = 0
      lindx = self.findNextLetter(ref[0],self.text,index)
      while lindx != -1 :
        counter += self.computeNum(ref[1:],lindx+1)
        lindx = self.findNextLetter(ref[0],self.text,lindx+1)
      return counter % 10000

  def setCount(self):
    self.count = self.computeNum(self.ref,0)

inputFile = open('C-small-attempt0.in','r')
outputFile = open('codejam_small.out','w')
numTc = int(inputFile.readline())
for i in range(0,numTc):
  line = inputFile.readline()
  c = CodeJam(line)
  c.setCount()
  strCount = str(c.getCount())
  if len(strCount) > 4 :
    print "Error length of answer is too long"
  while(len(strCount) < 4):
    strCount = '0'+strCount
  ans = 'Case #%s: %s\n' % ((i+1),strCount)
  outputFile.write(ans)

inputFile.close()
outputFile.close()
#text = 'wweellccoommee to code qps jam'
#text = 'elcomew elcome to code jam'
#text = 'welcome to codejam'
#text = 'welcome to code jam'

