T = int(input())
N = []
for i in range(0,T):
  N.append(int(input()))
  
m =0
for number in N:
  m+=1
  
  
  for j in range(number,-1,-1):
    s = str(j)
    
    if(len(s) == 1):
      print('Case #%d: %s' % (m,s))
      break
    
    tidy = False
    
    for k in range(0,len(s)-1):
      if s[k] > s[k+1]:
        tidy = False
        break
      else:
        tidy = True
    if tidy:
      print('Case #%d: %d' % (m,j))
      break
  