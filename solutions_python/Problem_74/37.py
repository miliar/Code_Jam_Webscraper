T=int(input())
for i in range(T):
  inp=input().split()
  N=int(inp[0])
  del inp[0]
  blue=[]
  orange=[]
  order=[]
  while inp:
    p=int(inp.pop())
    r=inp.pop()
    order.append(r)
    if r=='O':
      orange.append(p)
    else:
      blue.append(p)
  t=0
  bx=1
  ox=1
  ot=0
  bt=0
  while order:
    #print(t)
    #print(blue,orange,order)
    r=order.pop()
    if r=='O':
      p=orange.pop()
      t=max(t,abs(p-ox)+ot)+1
      ot=t
      ox=p
    else:
      p=blue.pop()
      t=max(t,abs(p-bx)+bt)+1
      bt=t
      bx=p
  print('Case #%d: %d' % (i+1,t))
