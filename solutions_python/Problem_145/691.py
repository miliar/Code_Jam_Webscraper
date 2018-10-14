import math

T = int(raw_input())

for i in xrange(T):
  A, B = [int(item) for item in raw_input().split('/')]
  found = False

  # Busca fraccion irreducible
  tmp = A
  while tmp > 1:
    if A%tmp == 0 and B%tmp == 0:
      A /= tmp
      B /= tmp
      tmp = A
    else:
      tmp -= 1

  # Aumenta A doblando cada vez, hasta superar B/2
  s = int(math.log(B, 2))
  if B == 2**s: # B es 2**n
    # Queremos A > B/2: 1/4 -> 2/4
    cnt = 0
    while A < B:
      A *= 2
      cnt += 1

    result = math.log(B, 2) + cnt
    found = True
  
  if found == True:
    print 'Case #%d: %d' % (i+1, cnt)
  else:
    print 'Case #%d: impossible' % (i+1)
