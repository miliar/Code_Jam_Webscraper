
def process(numbers):
  if (len(numbers) == 1):
    return
  else:
    for i in range(len(numbers) - 1):
      if (numbers[i] > numbers[i+1]):
        numbers[i] = numbers[i] - 1
        for j in range(i+1, len(numbers)):
          numbers[j] = 9
        break
def check(numbers):
  for i in range(len(numbers) - 1):
    if (numbers[i] > numbers[i+1]):
      return False
  return True
def doIt(numbers):
  while (check(numbers) != True):
    process(numbers)
  if (numbers[0] == 0):
    n = "".join(map(str,numbers[1:]))
  else:
    n = "".join(map(str,numbers))
  return n
'''inp = list(map(int, raw_input().strip()))
print(doIt(inp))'''
import sys
with open(sys.argv[1]) as f:
  testcase = f.readlines()
testcase = [line.rstrip('\n') for line in testcase]
num = int(testcase[0])
result = []
for i in range(1, num + 1):
  input = list(map(int,testcase[i].strip()))
  output = doIt(input)
  result.append('Case #' + str(i)+ ': ' + output)
with open(sys.argv[2], 'w') as fout:
  for i in result:
    fout.write(i + '\n')