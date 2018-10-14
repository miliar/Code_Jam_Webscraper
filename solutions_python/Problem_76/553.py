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
    self.inFile.readline()
    case = [int(tuple) for tuple in self.inFile.readline().split()]
    return case
    
class Processor:
  def __init__(self):
    self.output = ''
    self.input = []
    self.binaries = []
  def toBinary(self, num):
    result = []
    if num == 0:
      return [0]
    while num > 0:
      result.insert(0, (num % 2))
      num = int((num - (num % 2)) / 2)
    return result
  def toInt(self, binary):
    result = 0
    for i in range(len(binary)):
      n = binary[i]
      result *= 2
      result += n
    return result
  def stupidSum(self, binary1, binary2):
    #print(binary1)
    #print(binary2)
    result = []
    for i in range(max([len(binary1), len(binary2)])):
      if (i >= len(binary1)):
        result.insert(0, binary2[-i - 1])
      elif (i >= len(binary2)):
        result.insert(0, binary1[-i - 1])
      else:
        result.insert(0, (binary1[-i - 1] + binary2[-i - 1]) % 2)
    #print(result)
    return result
  def permutate(self, current, sum1, sum2, stupidSum1, stupidSum2):
    if (current == -1):
      if (sum1 == 0):
        return 0
      if (sum2 == 0):
        return 0
      #print ([sum1, sum2, stupidSum1, stupidSum2])
      if (self.toInt(stupidSum1) == self.toInt(stupidSum2)):
        return max([sum1, sum2])
      else:
        return 0
    else:
      n = self.input[current]
      b = self.binaries[current]
      result1 = self.permutate(current - 1, sum1 + n, sum2, self.stupidSum(stupidSum1, b), stupidSum2)
      result2 = self.permutate(current - 1, sum1, sum2 + n, stupidSum1, self.stupidSum(stupidSum2, b))
      return max([result1, result2])
        
  def processCase(self, input):
    self.input = input
    #print(input)
    self.binaries = [self.toBinary(tuple) for tuple in input]
    #print(self.binaries)
      
    maxResult = self.permutate(len(self.input) - 1, 0, 0, [0], [0])
    
    if (maxResult == 0):
      output = ['NO']
    else:
      output = [str(maxResult)]
    return output
    
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
