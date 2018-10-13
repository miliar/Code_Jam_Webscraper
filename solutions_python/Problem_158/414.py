f=open("D-small.in","r")
g=open("minos.out","w")

T = int(f.readline())

for i in range(0,T):
  [X,R,C] = map(int,f.readline().split())
  
  if X == 1:
    ans = 'GABRIEL'
  
  elif X == 2:
    if (R*C)%2 == 0:
      ans = 'GABRIEL'
    else:
      ans = 'RICHARD'
  
  elif X == 3:
    if (R*C)%3 != 0:
      ans = 'RICHARD'
    elif R == 1 or C == 1:
      ans = 'RICHARD'
    else:
      ans = 'GABRIEL'

  elif X == 4:
    if max(R,C) < 4:
      ans = 'RICHARD'
    else:
      if min(R,C) == 1:
        ans = 'RICHARD' 
      elif min(R,C) == 2:
        ans = 'RICHARD' 
      elif min(R,C) == 3:
        ans = 'GABRIEL' 
      elif min(R,C) == 4:
        ans = 'GABRIEL' 


  
  g.write("Case #"+str(i+1)+": "+ans+"\n")

  
  
  
