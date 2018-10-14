def check(m,n) : 
  s = str(m)
  t = str(n)
  if set(s) != set(t) : return False
  for i in range(len(s)-1) :
    if s[i+1:]+s[:i+1] == t : return True
  return False

T = int(raw_input())
for i in range(T) : 
  temp = raw_input().split()
  A = int(temp[0])
  B = int(temp[1])
  ans = 0
  for m in range(A,B+1) : 
    for n in range(m+1, B+1) : 
      if check(m,n) : ans += 1
  print "Case #%d: %d" %(i+1,ans)

