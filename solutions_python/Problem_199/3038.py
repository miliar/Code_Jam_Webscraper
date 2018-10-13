import sys

def flipCakes(pancakes, ind, k):
  for i in range(k):
    j = i + ind
    tmp = pancakes[j]
    if tmp == '+':
      pancakes[j] = '-'
    else:
      pancakes[j] = '+'
      
def checkHappy(pancakes):
  for cake in pancakes:
    if cake == '-':
      return(False)
  return(True)

def happySide(pancakes, k):
  if checkHappy(pancakes):
    return('0')
  counter = 0
  num = len(pancakes) - k + 1
  for i in range(num):
    cake = pancakes[i]
    if cake == '-':
      flipCakes(pancakes, i, k)
      counter += 1
  if checkHappy(pancakes):
    return(str(counter))
  return("IMPOSSIBLE")

def readPancakes(inputFile):
  with open(inputFile) as panFile:
    num = 0
    for line in panFile:
      columns = line.split()   
      num += 1
      if num == 1:
        numTests = columns[0]
      else:
        k = int(columns[1])
        result = happySide(list(columns[0]), k)
        print("Case #", num-1, ": ", result, sep='')

if __name__ == "__main__":
  inputFile = sys.argv[1]
  readPancakes(inputFile)
  