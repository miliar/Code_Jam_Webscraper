import string

inputFile = open('mushroom-large.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
cases     = inputData.split('\n')

def formatAnswer(index, answer):
  return "Case #" + str(index) + ": " + str(answer)

def methodOneSol(moments):
  answerSum = [ (max(0, moments[i-1] - moments[i]) ) for i in xrange(1,len(moments)) ]
  return sum(answerSum)

def methodTwoSol(moments):
  maxDiff = max([ moments[i-1] - moments[i] for i in xrange(1,len(moments))])
  eatingSum = 0
  for i in xrange(len(moments)-1):
    eatingSum += min(moments[i], maxDiff)

  return eatingSum

def computeAnswer(moments):
  methodOneAnswer = methodOneSol(moments)
  methodTwoAnswer = methodTwoSol(moments)

  return str(methodOneAnswer) + ' ' + str(methodTwoAnswer)


for index in xrange(1,len(cases), 2):
  case       = index/2 +1
  numMoments = int(cases[index])
  moments    = [int(x) for x in string.split(cases[index+1],' ')]
 
  answer = computeAnswer(moments)
  print formatAnswer(case, answer)

