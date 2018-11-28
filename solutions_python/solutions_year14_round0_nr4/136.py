def solve(a,b):
  l = len(a)
  P = 0
  i = 0
  j = 0
  while j<l:
    if b[j]>a[i]:
      P += 1
      i += 1
      j += 1
    else:
      j += 1
  return P
  

T = input()
for i in range(1,T+1):
  N = input()
  naomi = map(float,raw_input().split())
  ken = map(float,raw_input().split())
  naomi.sort()
  ken.sort()
  P0 = N-solve(naomi,ken)
  P1 = solve(ken,naomi)
  print "Case #%d: %d %d" % (i, P1, P0)
