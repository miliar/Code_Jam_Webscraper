t=int(input())
for k in range(t):
  s,u=input().split()
  u=int(u)
  s=[e for e in s]
  c=0
  for i in range(len(s)-u+1):
    if s[i]=='-':
      c+=1
      for j in range(i,i+u):
        if s[j]=='-':s[j]='+'
        else:s[j]='-'
  if '-' in s:print("Case #"+str(k+1)+':','IMPOSSIBLE')
  else:print("Case #"+str(k+1)+':',str(c))
  