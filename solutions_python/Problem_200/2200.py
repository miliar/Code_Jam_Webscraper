

class TidyNumbers(object):
  
  def isTydy(self, val):
    strVal = str(val)
    startVal = int(strVal[0])
    for i in range(1, len(strVal)):
      if startVal > int(strVal[i]):
        return False
      
      startVal = int(strVal[i])
    return True
      
      
  def execute(self, inFile, outFile):
    
    numberTest = int(inFile.next())
    print "Running %s tests" % numberTest
    for j, line in enumerate(inFile):
      print j, line
      data = line.strip()
      M, size = int(data), len(data)
      while not self.isTydy(M):
        res = [0] * size
        refVal = int(data[size-1])
        for i in range(size-2, -1, -1):
          currVal = int(data[i])
          if refVal < currVal:
            decVal = currVal-1 
            if decVal == 0:
              res[i+1] = 0
            #else:
            for k in range(i, size):
              res[k] = 9
            refVal = decVal
            res[i] = refVal
          else:
            res[i+1] = refVal
            refVal = currVal
            res[i] = currVal
            
        if sum(res) == 0:
          res = [9] * (size - 1)
        M = "".join(map(lambda x: str(x), res))
      outFile.write("Case #%s: %s\n" % (j+1, int(M)))