f = open('A-large.in', 'r')
ff=open('A-large.out', 'w')
n = int(f.readline())
for i in range(n):
  s,k = f.readline().split(" ")
  k = int(k)
  s=list(s)
  ans=0
  for c in range(len(s) - k + 1):
    if s[c] == '+':
      continue
    ans+=1
    for j in range(k):
      s[c+j] = '+' if s[c+j] == '-' else '-'

  for c in s:
    if c == '-':
      ff.write('Case #'+ str(i+1) +': IMPOSSIBLE\n')
      ans=-1
      break
  if ans>=0:
    ff.write('Case #'+ str(i+1) +': ' + str(ans) + '\n')