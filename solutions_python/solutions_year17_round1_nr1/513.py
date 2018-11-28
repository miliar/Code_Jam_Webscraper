"""

"""

class AlphabetCake(object):
  """
  
  """
  
  def execute(self, inFile, outFile):
    """
    """
    numberTest = int(inFile.next())
    print "Running %s tests" % numberTest
    case = 1
    while True:
      try:
          row, col = map(lambda x:int(x), inFile.next().strip().split(" "))
          table, newTable = [], []
          for i in xrange(row):
            rowStr = inFile.next().strip()
            table.append(rowStr)
            rec = []
            for i in xrange(col):
              rec.append(rowStr[i]) 
            newTable.append(rec)
            
          for i in xrange(row):
            dictLetter = {}
            for j in xrange(col):
              if table[i][j] != '?':
                dictLetter[table[i][j]] = j
            
            if not dictLetter and i > 0: 
              for j in xrange(col): 
                newTable[i][j] = newTable[i-1][j]
                
            else:
              for letter, pos in dictLetter.iteritems():
                start = pos-1
                while start >= 0:
                  if table[i][start] == '?':
                    newTable[i][start] = letter
                  else:
                    break
                  
                  start -= 1
                
                start = pos+1
                while start < col:
                  if table[i][start] == '?':
                    newTable[i][start] = letter
                  else:
                    break
                  
                  start += 1
  
          for i in range(row-2, -1, -1):
            dictLetter = {}
            for j in xrange(col):
              if newTable[i][j] != '?':
                dictLetter[newTable[i][j]] = j
            
            if not dictLetter: 
              for j in xrange(col): 
                newTable[i][j] = newTable[i+1][j]
       
          outFile.write("Case #%s:\n" % case)  
          for i in range(row):
            outFile.write("%s\n" % "".join(newTable[i]))
          case += 1   
      except StopIteration:
          break
      
      
      
    