import sys
import math

def choose(n, k):
  if (k <= n) and (k > 0):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
  else:
    return 0

def process_case(c):
  memo = {}

  for n in range(2, c+1):
    for m in range(1, n):
      if m == 1:
        memo[n] = {1:1}
      else:
        memo[n][m] = 1
        for i in range(1, m):
          memo[n][m] += memo[m][i] * choose(n-m-1, m-i-1)
          
  to_return = 0
  for y in (memo[n]):
    to_return += memo[n][y]
  return to_return

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  case = int(infile.readline())
  print process_case(case) % 100003

infile.close()