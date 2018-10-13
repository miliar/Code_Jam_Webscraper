def parseInt(num):
  length = len(num)
  out = 0
  for ch in num:
    out = out << 1
    if ch == '+':
      out +=1
  return(length, out)
  
def createFlipper(length):
  return 2**length - 1

def getNthBit(num, index):
  return not not(num & (1 << index))

def solve(st, flipLen):
  (length, num) = parseInt(st)
  flipper = createFlipper(flipLen)
  count = 0
  for i in range(0, length - flipLen + 1):
    if not getNthBit(num, i):
      count += 1
      num = num ^ flipper
    flipper = flipper << 1
  possible = True
  for i in range(length-flipLen+1, length):
    if not getNthBit(num, i):
      possible = False
      break
  return (count, possible)

t = int(input())
for i in range(1, t + 1):
  inp = input().split(" ")
  pancakes = inp[0]
  flipperLen = int(inp[1])
  flips, possible = solve(pancakes, flipperLen)
  print("Case #{}: {}".format(i, flips if possible else "IMPOSSIBLE"))