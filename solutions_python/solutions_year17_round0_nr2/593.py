for x in xrange(input()):
  n = input()  
  ls = list(str(n)) + ['9']
  ln = len(ls)
  for i in xrange(ln-2, -1, -1):
    if ls[i] <= ls[i+1]:
      continue
    ls[i] = str(int(ls[i])-1)
    ls[i+1:] = ['9']*(ln-i-1)
  kc = int(''.join(ls[:-1]))
  print 'Case #{0}: {1}'.format(x+1, kc)
