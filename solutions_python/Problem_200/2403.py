def findTiny(number):
    if number < 9:
        return number
    numberString = int2Array(number)


    for digit in range(len(numberString)-1, 0, -1): # at least two digits
        if numberString[digit] < numberString[digit-1]:
            for i in range(digit, len(numberString)):
                numberString[i] = 9
            #print(numberString)
            frontDigitsBefore = array2Int(numberString[0:digit])
            #print(frontDigitsBefore)
            frontDigitsAfter = int2Array(frontDigitsBefore-1)
            #print(frontDigitsAfter)
            #print(numberString[digit:])
            frontDigitsAfter.extend(numberString[digit:])
            numberString = frontDigitsAfter
            #print(numberString)
    return array2Int(numberString)

def array2Int(array):
    return int(''.join(map(str,array)))

def int2Array(number):
    array = []
    numberString = str(number)
    for i in numberString:
        array.append(int(i))
    return array
	
	
	
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())  # read a list of integers, 2 in this case
  result = findTiny(n)
  
  print("Case #{}: {}".format(i, result))