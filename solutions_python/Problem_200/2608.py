def isTidy(n):
  s = str(n)
  c = int(s[0])
  for i in range(1,len(s)):
    temp = int(s[i])
    if c > temp:
      return False
    c = temp
  return True

def makeTidy(n):
  s = str(n) #132
  prev = len(s)-2 #1
  now = prev+1 #2
  while(prev>=0):
    iprev = int(s[prev]) #3
    inow = int(s[now]) #2
    if iprev > inow:
      s = s[:prev]+str(iprev-1)+s[prev+1:]
      for i in range(now,len(s)):
        s = s[:i]+'9'+s[i+1:]
    prev-=1
    now=prev+1
  return int(s)
  
def solve(n): 
  #findLastTidy
  while(not isTidy(n)):
    n = makeTidy(n)
  return n

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  print("Case #{}: {}".format(i, solve(n)))
 