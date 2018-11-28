import sys
import math

def sub(n, digit, amount):
  return n - pow(10, digit) * amount

def solve(n) :
  lastDigit = 9
  place = 0
  itr = int(math.log10(n) + 1)
  i = 0
  while(i<itr):
    d = int(n / pow(10, i)) % 10
    # print(d)
    if(d > lastDigit):
      placeDigit = int(n / pow(10, place)) % 10
      n = sub(n, place, placeDigit + 1)
      # print(n, int(n / pow(10, place)) % 10)
      place+=1
      i-=1
      d = int(n / pow(10, i)) % 10
    lastDigit = d
    i += 1
  return n

# print(solve(132))
# print(solve(1000))
# print(solve(7))
# print(solve(111111111111111110))
# print(solve(110))
# print(solve(100100))

i = 1
t = -1
for line in sys.stdin:
  stripped = line.rstrip()
  if(t == -1):
    t = stripped
    continue
  ans = solve(int(stripped))
  answer = "Case #%d: %d"%(i, ans)
  print(answer)
  i+=1