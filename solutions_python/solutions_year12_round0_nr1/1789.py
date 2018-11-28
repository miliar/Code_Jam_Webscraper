import sys

class TestCase(object):
  def __init__(self, inputText):
    self.inputText = inputText
    
  def getGoogleseText(self, mapping):
    outputText = ""
    for char in self.inputText:
      outputText += mapping[char]
    return outputText
    
  def getEnglishText(self, mapping):
    reverseMapping = dict((v,k) for k,v in mapping.items())
    outputText = ""
    for char in self.inputText:
      outputText += reverseMapping[char]
    return outputText
    
  def getMapping(self, outputText):
    mapping = {}
    for i in range(len(self.inputText)):
      mapping[self.inputText[i]] = outputText[i]
    return mapping  
   
def readInteger():
  return int(sys.stdin.readline())

def readInputs():
  numberOfTestCases = readInteger()
  inputs = []
  for i in range(numberOfTestCases):
    inputs.append(sys.stdin.readline().strip())
  return inputs
  
mapping = TestCase('our language is impossible to understand').getMapping('ejp mysljylc kd kxveddknmc re jsicpdrysi')
mapping.update(TestCase('there are twenty six factorial possibilities').getMapping('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'))
mapping.update(TestCase('so it is okay if you want to just give up').getMapping('de kr kd eoya kw aej tysr re ujdr lkgc jv'))
mapping['a'] = 'y'
mapping['o'] = 'e'
mapping['z'] = 'q'
alphabet = ' abcdefghijklmnopqrstuvwxyz'

unusedKeys = []
for char in alphabet:
  if char not in mapping.keys():
    unusedKeys.append(char)

unusedValues = []
for char in alphabet:
  if char not in mapping.values():
    unusedValues.append(char)

if (len(unusedKeys) > 1):
  raise Exception('too many unused keys to be certain')
  
mapping.update(zip(unusedKeys, unusedValues))

test = TestCase('the quick brown fox jumped over the lazy dog')
#print test.getOutputText(mapping)

caseNumber = 1
for inputText in readInputs():
  print 'Case #%s:' % caseNumber, TestCase(inputText).getEnglishText(mapping)
  caseNumber += 1
