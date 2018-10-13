f=open("A-small.in","r")
g=open("tictac.out","w")

T = int(f.readline())

for i in range(0,T):
  
  M = []
  for l in range(0,4):
    H = []
    A = list(f.readline())
    A.pop()
    B = [w.replace('X','0').replace('O','1').replace('T','50').replace('.','-5') for w in A]
    M.append(map(int,B)) 
  
  D = 0
  for zz in range(0,4):
    for p in M[zz]:
      if p == -5:
        D = 1
    
  
  C = []
    
  for j1 in range(0,4):
    C.append(sum(a[j1] for a in M))  
  
  for j2 in range(0,4):
    C.append(sum(M[j2]))
  
  d1=0
  d2=0
  for l in range(0,4):
    d1 += M[l][l]
  C.append(d1)
  for l in range(0,4):
    d2 += M[l][3-l]
  
  C.append(d2)

  if 0 in C or 50 in C:
    R = 'X won'
  elif 4 in C or 54 in C:   
    R = 'O won'
  else:  
    if D == 1: 
      R = 'Game has not completed'
    else:
      R = 'Draw'

  g.write("Case #"+str(i+1)+": "+R+"\n")
  f.readline()
