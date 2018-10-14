# aKs = available keys, oC = opened chests, cTo = chest to open
# kTOc = key to open chest, kIc = keys in chest : READ ONLY
def solveHelper(aKs, oC, cTo, kTOc, kIc, indent, resultsNotPossible):
  ans = ''
  if len(aKs) > 0:
    for c in cTo:
      if kTOc[c] in aKs:
        coaKs = aKs[:]
        cooC = oC[:]
        cocTo = cTo[:]
        
        coaKs.remove(kTOc[c])
        tKs = coaKs + kIc[c]

        cooC.append(c)
        cocTo.remove(c)

        if len(cocTo) == 0:
          ans = cooC[:]
          break
        else:
          hashKey = ''
          for c in cocTo:
            hashKey += str(c)
            hashKey += ' '
            
          if hashKey in resultsNotPossible and sorted(resultsNotPossible[hashKey]) == sorted(tKs) :
            continue
          else:
            ans = solveHelper(tKs, cooC, cocTo, kTOc, kIc, indent+'  ', resultsNotPossible)
            if not ans:
              resultsNotPossible[hashKey] = tKs

          if ans:
            break
  return ans

def solutionPossible(keyRequired, totalKeyCount) :
  ret = True
  for k in keyRequired:
    if not k in totalKeyCount or keyRequired[k] > totalKeyCount[k]:
      ret = False
      break
  return ret  
      
def solve(fIn):
  line = fIn.readline()
  [nK, nC] = [int(x) for x in line.split()]

  line = fIn.readline()
  totalKeyCount = {}
  keyRequired = {}
  
  # initial keys
  iKs = line.split()

  for k in iKs:
    if k in totalKeyCount:
      totalKeyCount[k] += 1
    else:
      totalKeyCount[k] = 1
      
  kTOc = {}
  kIc = {}
  
  for i in range(1, nC+1):
    line = fIn.readline()
    array = line.split()
    
    # key to open chest
    kTOc[i] = array[0]

    if array[0] in keyRequired:
      keyRequired[array[0]] += 1
    else:
      keyRequired[array[0]] = 1

    # keys in chest
    kIc[i] = array[2:]
    for j in kIc[i]:
      if j in totalKeyCount:
        totalKeyCount[j] += 1
      else:
        totalKeyCount[j] = 1
    

  cTo = range(1, nC+1)
  oC = []

  ans = ''
  resultsNotPossible = {}
  if solutionPossible(keyRequired, totalKeyCount) :
    ans = solveHelper(iKs, oC, cTo, kTOc, kIc, '', resultsNotPossible)

  if ans == '':
    result = 'IMPOSSIBLE'
  else:
    result = ''
    for i in range(len(ans)):
      result += str(ans[i])
      result += ' '

  print result    
  return result

def main(filename):
  fIn = open(filename)
  fOut = open(filename+'.out', 'w')
  numTestCases=int(fIn.readline())
  for i in range(numTestCases):
    print 'testcase', i+1
    result = solve(fIn)
    fOut.write('Case #' + str(i+1) + ': ' + result + '\n')

  fIn.close()
  fOut.close()
  return
    
main('D:\\tech\\code_jam\\2013\\Problem D. Treasure\\D-small-attempt1.in')


