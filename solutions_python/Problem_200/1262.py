def solve(s):
  s.reverse()
  s = list(map(int, s))
  for i in range(len(s)):
    for j in range(i+1, len(s)):
      if s[i] < s[j]:
        s[j] -= 1
        for k  in range(j):
          s[k] = 9
  
  s.reverse()
  r = 0
  for i in s:
    r = r*10 + i
  return r
  
  
      


T = int(input())

for t in range(1, T+1):
  s = input()
  print("Case #" + str(t) + ":", solve(list(s))) 
  
  
