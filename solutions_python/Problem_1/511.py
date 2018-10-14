import os

def CommandLineOperations(argv):
  """
  Main method for reading argument from command prompt,
  read file with input data, process data and write result in output file
  argv command prompt arguments
  """
  outputFile = "result.out"
  inputFile = None
  scriptName = argv[0]
  del argv[0]

  try:
    argTup = getopt.getopt(argv, "di:o:", ["dist", "input=", "output="])
    try:
      for opt, val in argTup[0]:
        if opt in ("-d", "-dist"):
          makeExe(scriptName)
          sys.exit(0)
        if opt in ("-i", "-input="):
          inputFile = val
        if opt in ("-o", "-output="):
          outputFile = val
      #print inputFile, outputFile
    except ValueError:
      raise getopt.GetoptError("ERROR: Input File is requited")
      
    if not inputFile:
      raise getopt.GetoptError("ERROR: Input File is requited")
  except getopt.GetoptError:
    usage()
    sys.exit(2)

  return (inputFile, outputFile)



def solveProblem(argv, method, linesPerCase = 1, inputFile = None, outputFile = None):
  if inputFile is None and outputFile is None:
    inputFile, outputFile = CommandLineOperations(argv)

  inputFile = os.path.normpath(inputFile)
  outputFile = os.path.normpath(outputFile)
  
  """
  Method for solving problem.
  param inputFile Filename of input file with input data
  param outputFule Filename of output file to write resulting output data
  """
  f = open(inputFile, "r")
  fw = open(outputFile, "w")
  line = f.readline()
  casesNum = int(line)
  
  for i in range(1, casesNum+1):
    if i > 1:
      fw.write("\n")

    case = {}
    for k in range(i, i+linesPerCase):
      sNum = int(f.readline().replace("\n", ""))
      sArr = []
      for sN in range(0, sNum):
        sLine = f.readline().replace("\n", "")
        sArr.append(sLine)
        
      qNum = int(f.readline().replace("\n", ""))
      qArr = []
      for qN in range(0, qNum):
        qLine = f.readline().replace("\n", "")
        qArr.append(qLine)

      case = {"s":sArr, "q":qArr}  
      
    i = k
    result = method(case)
    fw.write("Case #%d: %s" % (i, result))
    
  fw.close()
  f.close()

def universeCaseMethodOld(caseLines):
  sArr = caseLines.get("s")
  qArr = caseLines.get("q")
  
  counter = []  
  for s in sArr:
    counter.append(qArr.count(s))

  answer = min(counter)

  return answer

def universeCaseMethod(caseLines):
  sArr = caseLines.get("s")
  qArr = caseLines.get("q")

  sArrTemp = sArr
  counter = 0
  incDict = {}
  ind = 0
  for q in qArr:
    if incDict.has_key(q) == False:
      incDict[q] = 0
    
    incDict[q] += 1

    #print q, incDict
    
    if len(incDict) == len(sArr):
      counter += 1
      incDict = {}

    if ind > 1 and incDict == {} :
      if qArr[ind-2] == q:
        counter += 1
      #print "plus one"

    ind += 1
  
  return counter

def findBestEngine(sArr, qArr, currEngine):
  countDict = {}

  switch = False

  qArrNext = qArr

  currLine = qArr[0]
  if currLine == currEngine:
    switch = True
    #qArrNext = qArr[1:]
  
  if switch or currEngine == None:

    currEngineChanged = False
    
    sArrLen = len(sArr)

    #print sArrLen

    for q in qArrNext:
      countDict[q] = 1

      if len(countDict) == sArrLen:
        currEngine = q
        currEngineChanged = True
        break

    if not currEngineChanged:
      #print "second try"
      lastItems = []
      currMin = 0
      for s in sArr:
        currCount = qArrNext.count(s)
        if currMin >= currCount:
          currEngine = s
          currEngineChanged = True

          
    if currEngineChanged and currEngine == currLine:
      currEngineChanged = False
      #print "not good"
      i = 0
      for q in qArrNext:
        if q == currEngine:
          currEngine = qArrNext[i-1]
          currEngineChanged = True
          break
        i += 1

      if not currEngineChanged:
        for q in qArr:
          if q != currEngine:
            currEngine = q
            currEngineChanged = True
            break

  return currEngine, switch


def universeCaseMethodV2(caseLines):
  sArr = caseLines.get("s")
  qArr = caseLines.get("q")

  index = 0
  counter = 0
  currEngine = None
  for q in qArr:
    currEngine, switch = findBestEngine(sArr, qArr[index:], currEngine)
    #print "Line: %s, Current: %s, Switch: %s" % (q, currEngine, switch)
    if switch:
      counter += 1
    index += 1

  return counter
  
if __name__ == "__main__":
  case1 = {"s":[ "Googol Haiti",
                "Googol Montserrat",
                "Googol Kazakhstan"],
          
          "q":[ "Googol Haiti",      
                "Googol Montserrat", 
                "Googol Kazakhstan", 
                "Googol Haiti",      
                "Googol Montserrat", 
                "Googol Kazakhstan", 
                "Googol Haiti",      
                "Googol Montserrat", 
                "Googol Kazakhstan"]}
  
  case2 = {"s":["Googol Rwanda",
                "Googol San Marino"],
           "q":["Googol Rwanda",    
                "Googol San Marino",
                "Googol Rwanda",
                "Googol San Marino",
                "Googol Rwanda",
                "Googol San Marino",
                "Googol Rwanda",
                "Googol San Marino"]}

  case3 = {"s":["Saporo",
                "Googol New Zealand",
                "Googol South Africa"],
           "q":["Googol New Zealand",
                "Saporo",
                "Googol New Zealand",
                "Googol New Zealand",
                "Googol New Zealand",
                "Googol New Zealand",
                "Googol South Africa",
                "Googol South Africa",
                "Googol South Africa",
                "Googol South Africa",
                "Saporo",
                "Googol South Africa"]}


##  print findBestEngine(["Googol Haiti",
##                "Googol Montserrat",
##                "Googol Kazakhstan"],
##                [ "Googol Haiti",      
##                "Googol Montserrat", 
##                "Googol Kazakhstan", 
##                "Googol Haiti",      
##                "Googol Montserrat"][0:],
##                None)
##  
##  print findBestEngine(["Googol Haiti",
##                "Googol Montserrat",
##                "Googol Kazakhstan"],
##                       
##                [ "Googol Haiti",      
##                "Googol Montserrat", 
##                "Googol Kazakhstan", 
##                "Googol Haiti",      
##                "Googol Montserrat"][0:],
##                "Googol Haiti")
  
  #print universeCaseMethodV2(case3)
  solveProblem([], universeCaseMethodV2, inputFile = "c://Other//GJC//A-large.in", outputFile = "c://Other//GJC//A-large.out")
