T=int(input())
for i in range(T):
  combine={}
  oppose=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',[[] for i in range(26)]))
  check=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',[0]*26))
  inp=input().split()
  C=int(inp[0])
  j=1
  for k in range(j,j+C):
    (x,y,z)=inp[k]
    combine[(x,y)]=z
    combine[(y,x)]=z
  j=j+C+1
  D=int(inp[j-1])
  for k in range(j,j+D):
    (x,y)=inp[k]
    oppose[x].append(y)
    oppose[y].append(x)
  j=j+D+1
  N=int(inp[j-1])
  lst=[]
  seq=[inp[j][k] for k in range(N)]
  seq.reverse()
  seq=list(seq)
  clr=0
  while seq:
    #print(seq,lst)
    #print(check.items())
    x=seq.pop()
    if len(lst)>0:
      y=lst[-1]
      if (x,y) in combine:
        z=combine[(x,y)]
        lst.pop()
        seq.append(z)
        check[y]-=1
        continue
    for y in oppose[x]:
      if check[y]>0:
        clr=1
        break
    if clr:
      lst=[]
      for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        check[c]=0
      clr=0
      continue
    lst.append(x)
    check[x]+=1
  print('Case #%d: [' % (i+1),end='')
  fst=0
  for x in lst:
    print(fst*', '+x,end='')
    fst=1
  print(']')

	
    
  
    