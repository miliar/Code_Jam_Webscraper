N=4
T,X,O='T','X','O'
D='Draw'
G='Game has not completed'

# if someone wins return person's name otherwise return None
def f(b):
  for e in b:
    if e.count(X)==N: return X
    if e.count(O)==N: return O
  for e in zip(*b):
    if e.count(X)==N: return X
    if e.count(O)==N: return O
  p=[ b[i][i] for i in xrange(N)]
  if p.count(X)==N: return X
  if p.count(O)==N: return O
  xx=[ (N-(i+1),i) for i in xrange(N) ]
  q=[ b[i][-(i+1)] for i in xrange(N)]
  if q.count(X)==N: return X
  if q.count(O)==N: return O
  return None

for case in xrange(int(raw_input())):
  a=[ raw_input() for _ in xrange(N) ]
  raw_input()
  x=[e.replace(T,X) for e in a]
  o=[e.replace(T,O) for e in a]
  mes=None
  res=f(x)
  if res!=None: mes=res+' won'
  res=f(o)
  if res!=None: mes=res+' won'
  if mes==None:
    if [item for sublist in a for item in sublist].count('.')==0:
      mes=D
    else:
      mes=G
  print 'Case #%d: %s'%(case+1, mes)
