import sys

def getNumbers(m, A, B):
  s = str(m)
  l = []
  for i in range(len(s)):
    t = s[i:] + s[0:i]
    if t[0] != '0':
      n = int(t)
      if n <= B and n >= A and m < n:
        l.append((m, n))
  return l

def getResult(input):
  (A, B) = input
  if B <= 20:
    return 0
  l = []
  for i in range(A, B):
    nums = getNumbers(i, A, B)
    l.extend(nums)
  l.sort()
  result = len(set(l))
  return result

def process(line):
  nums = line.strip().split(' ')
  A = int(nums[0])
  B = int(nums[1])
  return (A, B)

data = sys.stdin.readlines()

data = data[1:]
i = 1
for line in data:
  input = process(line)
  print("Case #" + str(i) + ': ' + str(getResult(input)))
  i += 1