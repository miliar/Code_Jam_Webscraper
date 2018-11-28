f = open('D-large.in', 'r+')

outputFile = open('DeceitfulWarOuput.txt', 'w+')

def toFloat(seq):
  for x in seq:
      try:
          yield float(x)
      except ValueError:
          yield x


numberOfCase = int(f.readline())
for case in range(1, numberOfCase + 1):
  blocksCount = int(f.readline())
  NaomiWeight = sorted(list(toFloat(f.readline().split(' '))))
  KenWeight = sorted(toFloat(f.readline().split(' ')))
  
  outputFile.write("Case #" + str(case) + ": ")
  # Deceitful WAR
  score = 0
  naomiIndex = len(NaomiWeight) - 1
  for kenW in reversed(KenWeight):
    if kenW < NaomiWeight[naomiIndex]:
      score += 1    
      naomiIndex -= 1
  outputFile.write(str(score))
  
  # WAR
  score = 0
  for n in reversed(NaomiWeight):
    maxKen = max(KenWeight)
    if n > maxKen:
      score +=1
      del KenWeight[0]
    else:
      del KenWeight[-1]
  outputFile.write(" " + str(score) + "\n")








  