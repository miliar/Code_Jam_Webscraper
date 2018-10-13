

def digits(N):
  digitList = []
  while N//10 != 0:
     digitList.append(N%10)
     N = N//10
  digitList.append(N)
  return digitList

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  N = int(input())
  checkTidy = 0
  while checkTidy == 0:
    digitList = digits(N) 
    locTidy = 0
    numberOfDigits = len(digitList)
    if numberOfDigits == 1:
      numKeeper = digitList[0]
      checkTidy = 1
    else:
      numKeeper = digitList[0] 
      for x in range(1, numberOfDigits):
        if digitList[x] > digitList[x-1]:
          numKeeper = (pow(10,x)*digitList[x]) - 1
          locTidy = 1
        else:
          numKeeper += digitList[x] * pow(10,x)
      N = numKeeper
      if locTidy == 0:
        checkTidy = 1
  print("Case #{}: {}".format(i,numKeeper))
