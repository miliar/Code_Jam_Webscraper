def preveri(s1, s2):
  stej=0
  while stej<len(s1):
    s1=s1[1:]+s1[0]
    if s1==s2:
      return True
    stej+=1
  return False
    
for k in range(int(raw_input())):
  c=0
  n=[int(i) for i in raw_input().split()]
  for i in range(n[0],n[1]):
    for j in range(i+1,n[1]+1):
      if preveri(str(i),str(j)):
	c+=1
  print 'Case #%d: %d' %(k+1, c)