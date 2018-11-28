def cake(R,C,G):
  e=['?']*R
  t=0
  symb=['?']*R
  for r in range(0,R):
    s=0
    sym='?'
    for c in range(0,C):
      if G[r][c]=='?':
        G[r][c]=sym
      else:
        for cc in range(s,c+1):
          sym=G[r][c]
          G[r][cc]=sym
          s=c+1
    
  for r in range(0,R):
    if G[r][0] == '?':
      G[r]=symb
    else:
      s=0
      sym='?'
      for c in range(0,C):
        if G[r][c]=='?':
          G[r][c]=sym
        else:
          for cc in range(s,c+1):
            sym=G[r][c]
            G[r][cc]=sym
            s=c+1
      for rr in range(t,r+1):
        symb=G[r]
        G[rr]=symb
        t=r+1
  if t<R-1:
    for rr in range(t,R):
      G[rr]=symb
  return G
  

T = int(input())  # read a line with a single integer
for i in range(0, T ):
  R, C = [int(s) for s in input().split(" ")]
  G=['']*R
  for j in range (0, R):
    G[j]= [str(s) for s in input()]
  G=cake(R,C,G)
  print("Case #{}:".format(i+1))
  for j in range(0, R ):
     print(''.join(G[j]))
