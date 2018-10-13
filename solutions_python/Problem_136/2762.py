T = input()
for t_ in range(1, T+1):
  C, F, X = tuple( [float(x) for x in raw_input().split()] )

  x = 0.0
  f = 2.0
  t = 0.0
  while(X>0):
    t1 = X/f
    t2 = C/f + X/(f+F)

    if t1 < t2:
      t += t1
      X = 0
    else:
      t += C/f
      f += F

  print "%s%d%s%.7f" % ("Case #",t_,": ",t)