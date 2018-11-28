# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  numList= str(input())  # read a list of integers, 2 in this case
 # numList = list(inputString)
  count = 0
  result = []
  numLength = len(numList) 
  flag = bool(0)
  sameDigitQueue = []
  while count < numLength:
   if flag:
    result += ['9']
   elif count == numLength - 1:
     if flag is False :
      if sameDigitQueue :
       result += sameDigitQueue
      result += numList[count]
   else :
    first = numList[count]
    second = numList[count+1]
    if int(first) > int(second):
     if sameDigitQueue:
       sameDigitQueue += first
       firstDigitInQueue = int(sameDigitQueue[0])
       temp = int(firstDigitInQueue)-1
       if temp > 0:
         result += str(temp)
       result += [str(9) for z in sameDigitQueue[1:]]
     else: 
      digit = int(first)-1
      if digit>0 :
       result += str(digit)
     flag = bool(1)
    elif int(first) == int(second):
      sameDigitQueue += first
    elif int(first) < int(second):
     if sameDigitQueue :
      result+= sameDigitQueue
     else :
      result += str(first)
   count+=1
 # print("Case #{}: {}".format(i, result))
  print("Case #{}: {}".format(i, reduce(lambda x,y : x+y, result)))
  # check out .format's specification for more formatting options
