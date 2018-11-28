import sys

def largestTidy(ind, n):
  largest = list(n)
  for i in range(len(largest)):
    if i == ind:
      num = int(largest[i]) - 1
      largest[i] = str(num)
    if i > ind:
      largest[i] = '9'
  return(largest)

def findTidy(n):
  digits = list(n)
  if len(digits) == 1:
    return(digits)
  i = 0
  prevNum = -1
  while i < len(digits):
    num = int(digits[i])
    if num < prevNum:
      j = i - 2
      while j >= 0:
        if int(digits[j]) < prevNum:
          largest = largestTidy(j+1, n) 
          return(largest)
        j -= 1
      return(largestTidy(0, n))
    i += 1
    prevNum = num
  return(digits)
      
def readNumbers(inputFile):
  with open(inputFile) as panFile:
    num = 0
    for line in panFile:
      num += 1
      if num > 1:
        largest = findTidy(line.rstrip())
        print("Case #", num-1, ": ", sep='', end='')
        i = 0
        while i < len(largest): 
          if largest[i] != '0':
            break
          i += 1
        print("".join(largest[i:]))

if __name__ == "__main__":
  inputFile = sys.argv[1]
  readNumbers(inputFile)

