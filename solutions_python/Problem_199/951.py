import sys
import math

def flip(arr, i, k):
  for i in xrange(i, i + k):
    if(arr[i] == '+'):
      arr[i] = '-'
    else:
      arr[i] = '+'
  return arr

minFlips = -1
memo = {}
def solve(arr, k):
  minFlipped = -1
  e = False

  s = "".join(arr)
  if(s in memo):
    return -1
  memo[s] = True

  for i in xrange(0, len(arr) - k + 1):
    if(arr[i] == '-'):
      e = True
    if(e):
      # copy list
      flipped = flip(arr[:], i, k)
      ans = solve(flipped, k) + 1
      if(ans != 0 and (ans < minFlipped or minFlipped == -1)):
        minFlipped = ans
        # print(flipped)

  # check flipped
  for i in xrange(0, len(arr)):
    if(arr[i] == '-'):
      e = True
  if(not e):
    # print("FOUND", arr)
    return 0
  if(minFlipped == -1):
    return -1
  return minFlipped

i = 1
t = -1
for line in sys.stdin:
  stripped = line.rstrip().split(" ")
  if(t == -1):
    t = 1
    continue
  memo = {}
  ans = solve(list(stripped[0]), int(stripped[1]))
  if(ans == -1):
    ans = "IMPOSSIBLE"
  answer = "Case #%d: %s"%(i, ans)
  print(answer)
  i+=1