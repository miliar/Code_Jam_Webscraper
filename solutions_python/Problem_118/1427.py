import sys
import math

filein = open("C-small-attempt1.in", 'r')
fileout = open("output.out", 'w')

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

test_cases = int(filein.readline().strip())

for test_case in range(test_cases):
    minValue, maxValue = filein.readline().split()
    minValue, maxValue = int(minValue), int(maxValue)
    count = 0
    for num in range(minValue, maxValue + 1):
        remainder = math.sqrt(num) % 1.0
        s = str(int(math.sqrt(num)))
        if str(num) == str(num)[::-1] and remainder == 0.0 and s == s[::-1]:          
#             print num, math.sqrt(num)
            count += 1
    fileout.write("Case #{}: {}\n".format(test_case+1, count))    

