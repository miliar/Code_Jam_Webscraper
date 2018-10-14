def isHappy(s):
  for c in s:
    if c != '+':
      return False
  return True

def flipFunc(s):
  res=""
  for c in s:
    if c == "+":
      res+="-"
    else:
      res+="+"
  return res
  
def solve(s,k):
  flips = 0
  pos = 0
  while((pos+k) <= len(s)):
    if(isHappy(s)):
      return flips
    if(s[pos]=="-"):
      flips+=1
      s = s[:pos]+flipFunc(s[pos:pos+k])+s[pos+k:]
    pos+=1
  if(isHappy(s)):
      return flips
  return "IMPOSSIBLE"

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  s, k = [n for n in input().split(" ")] #readpairofinputs
  print("Case #{}: {}".format(i, solve(s, int(k))))
 