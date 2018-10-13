fname = 'cookie'
fin = open('%s.in' % fname,'r')
fout = open('%s.out' % fname,'w')

T = int(fin.readline())

for i in range(T):
  [C,F,X] = [float(x) for x in fin.readline().split(' ')]
  
  
  # tn = lambda n: sum([C/(2+i*F) for i in range(n+1)]) + (X-C)/(2+n*F)
  # tprev = tn(0)
  # tnext = tn(1)
  # n = 2
  # while tprev > tnext:
    # tprev = tnext;
    # tnext = tn(n);
    # n += 1
  # t = tprev
  
  cps = 2
  t = 0
  while True:
    t_to_farm = C/cps
    t += t_to_farm
    if (X-C)/cps < X/(cps+F):
      t += (X-C)/cps
      break
    cps += F
  
  fout.write('Case #%u: %0.9g\n' % (i+1,t))

fin.close()
fout.close()