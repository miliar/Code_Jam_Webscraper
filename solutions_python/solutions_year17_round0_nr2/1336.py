def subtract(digits, position):
  digits[position] = digits[position] - 1
  if position == 0:
    for curPos in range (1, len(digits) - 1):
      digits[curPos] = 9
    newNumber = int(''.join(map(str, digits)))
    digits = [int(x) for x in str(newNumber)]
    return
  if digits[position] < 0:
    subtract(digits, position - 1)
    digits[position] = 9
  
  
def main(number):
  if number is None:
    return
  digits = [int(x) for x in str(number)]
  for curPos in range(len(digits)-1):
    if digits[curPos] <= digits[curPos + 1]:
      pass
    else:
      subtract(digits, curPos)
      for curPos2 in range(curPos + 1, len(digits)):
        digits[curPos2] = 9
  return int(''.join(map(str, digits)))
      

cases = int(input())
for curCase in range(0,cases):
  curInput = int(input())
  curResult = main(curInput)
  curResult2 = main(curResult)
  while curResult != curResult2:
    curResult = main(curResult2)
    curResult2 = main(curResult)
  print("Case #"+str(curCase+1)+": "+str(curResult))