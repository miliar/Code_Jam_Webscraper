def solve(s, k):
  d = {'-':'+', '+':'-'}
  c = 0
  for i in range(len(s) - k + 1):
    if s[i] == '-':
      c += 1
      for j in range(i, i+k):
        s[j] = d[s[j]]
  for i in s:
    if i == '-':
      return 'IMPOSSIBLE'
  return c
      


T = int(input())

for t in range(1, T+1):
  s = input().split(' ')
  k = int(s[1])
  s = s[0]
  print("Case #" + str(t) + ":", solve(list(s),k)) 
  
  
