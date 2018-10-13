import sys, string

class Parser:
  def __init__(self, inFile):
    self.inFile = inFile
    self.caseRead = 0
    self.numCase = int(self.inFile.readline())    
  def hasNextCase(self):  
    return (self.caseRead < self.numCase)
  def readNextCase(self):
    self.caseRead = self.caseRead + 1
    case = self.inFile.readline().split()
    numCombine = int(case[0])
    combine = case[1:1 + numCombine]
    numOppose = int(case[1 + numCombine])
    oppose = case[2 + numCombine:2 + numCombine + numOppose]
    numElement = int(case[2 + numCombine + numOppose])
    elements = case[3 + numCombine + numOppose]
    return [combine, oppose, elements]
    
class Processor:
  def __init__(self):
    self.output = ''
  def processCase(self, input):
    #print (input)  
    
    combineList = input[0]
    combine = dict()
    if (len(combineList) > 0):
      for combination in combineList:
        a = combination[0]
        b = combination[1]
        combined = combination[2]
        combine[a + b] = combined
        combine[b + a] = combined
    #print (combine)
    
    opposeList = input[1]
    oppose = dict()
    if (len(opposeList) > 0):
      for opposition in opposeList:
        a = opposition[0]
        b = opposition[1]
        if (a in oppose):
          oppose[a].append(b)
        else:
          oppose[a] = [b]
        if (b in oppose):
          oppose[b].append(a)
        else:
          oppose[b] = [a]
    #print (oppose)
    
    elements = input[2]
    result = ''
    
    for i in range(len(elements)):
      #print (result)
      c = elements[i]
      #print (c)
      if (len(result) < 1):
        result = c
      else:
        last = result[-1:]
        
        #find for possible combine
        if ((last + c) in combine):
          result = result[:-1] + combine[(last + c)]
          continue
            
        #find for possible oppose
        if (c in oppose):
          os = oppose[c]
          foundOppose = False
          for o in os:
            if(result.find(o) != -1):    
              result = ''
              foundOppose = True
              break
          if (foundOppose):
            continue
          
        result += c
      
      
    output = '['
    for i in range(len(result)):
      output += result[i]
      if (i < (len(result) - 1)):
        output += ', '
    output += ']'
    
    return [output]
    
class Printer:
  def __init__(self, outFile):
    self.outFile = outFile
    self.caseNum = 1
  def printCaseOutput(self, output):
    outputStr = ' '.join(output)
    self.outFile.write('Case #' + str(self.caseNum) + ': ' + outputStr + '\n')
    self.caseNum = self.caseNum + 1
        
# run the program
def run(inFileName):
  inFile = open(inFileName, 'r')
  #outFile = sys.stdout
  outFile = open(inFileName + '.out', 'w')
  
  parser = Parser(inFile)
  processor = Processor()
  printer = Printer(outFile)
  while (parser.hasNextCase()):
    printer.printCaseOutput(processor.processCase(parser.readNextCase()))
  
  inFile.close()
  outFile.close()
  
# the main function
def main():
  args = sys.argv[1:]
  if len(args) < 1:
    printf("ERROR: Not enough arguments")
    sys.exit(-1)
  # run: 1st argument --> input file name 
  run(args[0])

# call the main function
if __name__ == '__main__':
  main()
