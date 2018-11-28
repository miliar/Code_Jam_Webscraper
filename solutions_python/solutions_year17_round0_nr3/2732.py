import sys
sys.setrecursionlimit(1500)

test_cases = int(raw_input())

global breaker
def initialCount (current):
  count = 0
  idx = 0
  while idx < len(current) and current[idx] != "1":
    count += 1
    idx += 1
  return count

def find (current):
  global breaker
  result = [-1, -1]
  cursor = 0
  for i in xrange(0, len(current)):
    if current[i] != "1":
      old = [old[0]+1, initialCount(current[i+1:])]
      if min(result) < min(old):
        result = old
        cursor = i
      elif min(result) == min(old):
        if max(result) < max(old):
          result = old
          cursor = i
    else:
      old = [-1, -1]
  current[cursor] = "1"
  if breaker != 0:
    breaker -= 1
    return find(current)
  return result

for case in xrange(1, test_cases + 1):
  n, k = [int(s) for s in raw_input().split(" ")]
  if n == k:
    print "Case #{}: {} {}".format(case, "0", "0")
  else:
    global breaker
    breaker = k - 1
    toilette = []
    toilette.append("1")
    for i in xrange(0, n):
      toilette.append("0")
    toilette.append("1")
    result = find(toilette)
    print "Case #{}: {} {}".format(case, max(result), min(result))
