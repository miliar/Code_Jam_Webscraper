def readint():  return int(input())
def readline(): return input().split()
def readints(): return list(map(int, readline()))

def solve(s, K):
  # Greedy algorithm should always produce optimal #flips
  happy = [c == '+' for c in s]
  count = 0
  for i in range(len(happy) - K + 1):
  # print(i, "".join('+' if x else '-' for x in happy))
    if not happy[i]:
      # need to flip at position `i`
      if i + K > len(happy): return None
      count += 1
      for j in range(K):
        happy[i+j] = not happy[i+j]
  if all(happy):
    return count
  return None

_T = readint()
for _t in range(_T):
  # read input
  s, K = readline()
  K = int(K)

  # compute answer
  res = solve(s,K)
  if res == None: res = "IMPOSSIBLE"
  print("Case #{}: {}".format(_t + 1, res))

