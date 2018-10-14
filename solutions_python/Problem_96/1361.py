cases = int(raw_input())
for i in range(0,cases):
  ins = raw_input()
  n, s, p, t = ins.split(' ',3)
  p = int(p)
  t = t.split()
  ans = 0
  possible = 0
  for j in t:
    j = int(j)
    if j >= p*3-2:
      ans = ans+1
    elif j>= p*3-4 and j>=2:
      possible = possible+1
  
  print 'Case #' + str(i+1) + ': ' + str(ans + min(possible, int(s)))
  
