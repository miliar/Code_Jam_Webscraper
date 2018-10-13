import string

inputFile = open('dijkstra.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
cases     = inputData.split('\n')

def formatAnswer(index, answer):
  return "Case #" + str(index) + ": " + str(answer)

multDict = dict({ ('1','1') : '1', ('1','i') : 'i', ('1','j') : 'j', ('1','k') : 'k', \
    ('i','1') : 'i', ('i','i') : '-1', ('i','j') : 'k', ('i','k') : '-j', \
    ('j','1') : 'j', ('j','i') : '-k', ('j','j') : '-1', ('j','k') : 'i', \
    ('k','1') : 'k', ('k','i') : 'j', ('k','j') : '-i', ('k','k') : '-1' })

def mult(a,b):
  if (a,b) in multDict:
    return multDict[(a,b)]
  if a == '-1':
    return '-' + b
  else:
    ans = multDict[(a[1],b)]
    if ans[0] == '-':
      return ans[1]
    else:
      return '-' + ans


def checkString(ijkStr, numRepeat):

  ijkIndex = 0
  currentLetter = '1'
  realString = ijkStr * numRepeat
  for letter in realString:
    currentLetter = mult(currentLetter, letter)
    if ijkIndex == 0 and currentLetter == 'i':
      ijkIndex += 1
      currentLetter = '1'
    elif ijkIndex == 1 and currentLetter == 'j':
      currentLetter = '1'
      ijkIndex += 1

  if currentLetter == 'k' and ijkIndex == 2:
    return 'YES'
  else:
    return 'NO'



i = 1
while i < len(cases):
  [strLen, numRepeat] = [int(x) for x in string.split(cases[i],' ')]
  ijkStr              = cases[i+1]

  answer = checkString(ijkStr, numRepeat)
  print formatAnswer(i/2 +1, answer)

  i+= 2


