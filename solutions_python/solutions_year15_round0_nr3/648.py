def pdt(a, b, s):
  if a == "1":
    return b, s
  if b == "1":
    return a, s
  if a == "i":
    if b == "i":
      return "1", -s
    if b == "j":
      return "k", s
    if b == "k":
      return "j", -s
  if a == "j":
    if b == "i":
      return "k", -s
    if b == "j":
      return "1", -s
    if b == "k":
      return "i", s

  if a == "k":
    if b == "i":
      return "j", s
    if b == "j":
      return "i", -s
    if b == "k":
      return "1", -s

def pps(seuil, sortedArray):
  index = 0
  while index < len(sortedArray) and sortedArray[index] <= seuil:
    index += 1

  if index == len(sortedArray):
    return -1, -1
  return sortedArray[index], index

inputFile = open('C-small-attempt1.in', 'r')

outputFile = open('output', 'w')

class Found(Exception) : pass

nbTests = int(inputFile.readline())

for i in range(nbTests):
  l, x = inputFile.readline().split()
  l = int(l)
  x = int(x)

  word = inputFile.readline()
  if word[len(word) - 1] == '\n':
    word = word[:len(word) - 1]
  word *= x
  newLetter = "1"
  newSign = 1
  iIndexes = []
  for j in range(len(word)):
    newLetter, newSign = pdt(newLetter, word[j], newSign)
    if newLetter == "i" and newSign == 1:
      iIndexes += [j]
  newLetter = "1"
  newSign = 1
  kIndexes = []
  for j in reversed(range(len(word))):
    newLetter, newSign = pdt(word[j], newLetter, newSign)
    if newLetter == "k" and newSign == 1:
      kIndexes += [j]

  kIndexes.reverse()
  #print("\n")
  print("nbtest", nbTests, i, len(iIndexes), len(kIndexes))
  #print(kIndexes)
  
  try:
    if len(kIndexes) > 0:
      for j in range(len(iIndexes)):
        mink, minik = pps(iIndexes[j] +1, kIndexes)
        #print("mink, minin", mink, minik)
        if mink != -1:
          maxk = kIndexes[len(kIndexes) - 1]
          ik = minik

          newLetter = "1"
          newSign = 1

          for k in range(iIndexes[j] + 1, maxk):
            newLetter, newSign = pdt(newLetter, word[k], newSign)
            #print(j, k, newLetter, newSign)
            if k + 1 == kIndexes[ik]:
              if newLetter == "j" and newSign == 1:
                raise Found
              ik += 1
        #else:
          #print("kindex trop petit")


  except Found:
    outputFile.write("Case #" + str(i + 1) + ": YES\n")
  else:
    outputFile.write("Case #" + str(i + 1) + ": NO\n")

  '''
  try:
    for j in range(len(iIndexes)):
      print(j)
      for k in range(len(kIndexes)):
        begin = iIndexes[j] + 1
        end = kIndexes[k]

        newLetter = "1"
        newSign = 1
        for l in range (begin, end):
          newLetter, newSign = pdt(newLetter, word[l], newSign)
      if newLetter == "j" and newSign == 1:
        raise Found
  except Found:
    outputFile.write("Case #" + str(i + 1) + ": YES\n")
  else:
    outputFile.write("Case #" + str(i + 1) + ": NO\n")
  '''