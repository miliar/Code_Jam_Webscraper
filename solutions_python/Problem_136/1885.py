import decimal

d = decimal.Decimal
T = int(raw_input())

decimal.getcontext().prec = 20

for c in xrange(T):
  
  C,F,X = map(float,raw_input().split())
  
  C = d(C)
  F = d(F)
  X = d(X)
  
  A = 0
  T = X/2
  P = 2
  
  while(1):
    K = A+C/P+X/(P+F)
    if(K>T): break
    T = K
    A = A + C/P
    P += F
    
  print 'Case #%d:'%(c+1),("%.7lf"%T)

