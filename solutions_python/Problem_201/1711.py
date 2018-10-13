import math
testNum = int(input())
testCount =0
while testCount < testNum:
   data = input().split()
   stalls = int(data[0])
   people = int(data[1])
   value = 1
   while (value * 2 <= people):
      value *= 2
   otherValue = int(((stalls-people)/value))
   left = math.floor(otherValue*0.5)
   right = math.ceil(otherValue*0.5)
   print("Case #{:d}: {:d} {:d}".format(testCount+1, max(left, right), min(left, right)))
   testCount += 1