def ints():
  return [int(x.strip()) for x in raw_input().split(' ')]
cases = input()


for casenum in range(1, cases+1):
  n,x=ints()
  cap = sorted(ints())
  j = len(cap)-1
  i = 0
  d = 0
  while i <= j:
    d+=1
    v = cap[i]
    while j > i and cap[j] + v > x:
      j-=1
      d+=1
    if j==i:
      break
    j-=1
    i+=1
  print "Case #" + str(casenum) + ":", d
