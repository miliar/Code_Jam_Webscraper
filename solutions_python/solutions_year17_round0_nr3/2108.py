"""

"""

class BathroomStalls(object):
  """
  """
  
  def getPos(self, tab, pos):
    """
    """
    
    left, right = 0, 0
    i = 1
    while tab[pos + i] == 0:
      i += 1
    right = i - 1
    
    i = 1
    while tab[pos - i] == 0:
      i += 1
    left = i - 1
    return max(left, right), min(left, right)
      
  def addUser(self, tab):
    """
    """
    maxZero, end, currentCount = 0, 0, 0
    for i, val in enumerate(tab):
      if val == 0:
        currentCount += 1     
      else:
        if currentCount > maxZero:
          end = i - 1
          maxZero = currentCount
        currentCount = 0
    return end - (maxZero/2) 
        
  
  def execute(self, inFile, outFile):
    """
    """
    numberTest = int(inFile.next())
    print "Running %s tests" % numberTest
    for i, line in enumerate(inFile):
      N, users = map(lambda x: int(x), line.strip().split(" "))
      row = [1] + [0] * N + [1]  
      for k in range(0, users):
        lastPos = self.addUser(row)
        row[lastPos] = 1
      maxVal, minVal = self.getPos(row, lastPos)
      outFile.write("Case #%s: %s %s\n" % (i+1, maxVal, minVal))
        
      #  print i
