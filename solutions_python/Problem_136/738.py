def solve(C , F , X ):
  t = 0
  n = 0
  tp = 0
  while 1:
  #~ for _ in range(10):
    tn = C/(2+F*n)
    t = t + tn
    t0 = tp + X/(2+F*(n))
    t1 = t + X/(2+F*(n+1))
    #~ print t, t0, t1 
    if t0 <= t1:
      return t0
    n+=1
    tp = t
  
T = int(raw_input())
for i in range(T):
  C , F , X = map(float,raw_input().split())
  sol = solve(C , F , X )
  print 'Case #' + str(i+1) + ': ' + str(sol)

