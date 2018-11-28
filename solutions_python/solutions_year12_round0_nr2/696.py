import sys


def getResult(input):
  (N, S, p, scores) = input
  SUsed = 0
  result = 0
  
  for score in scores:
    div = int(score / 3)
    mod = score % 3
    if score > 0:
      if div >= p:
        result += 1
        continue
        
      if mod == 0 and div+1 >= p and SUsed < S:
        result += 1
        SUsed += 1
        continue
         
      if mod > 0 and div+1 >= p:
        result += 1
        continue
         
      if mod == 2 and div+2 >= p and SUsed < S:
          result += 1
          SUsed += 1
          continue
    else:
      if p == 0:
        result += 1
  return result

def process(line):
  nums = line.strip().split(' ')
  N = int(nums[0])
  S = int(nums[1])
  p = int(nums[2])
  scores = [int(x) for x in nums[3:N+3]]
  return (N, S, p, scores)

data = sys.stdin.readlines()

data = data[1:]
i = 1
for line in data:
  input = process(line)
  print("Case #" + str(i) + ': ' + str(getResult(input)))
  i += 1
