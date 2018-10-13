t = int(raw_input())

def is_tidy(n):
  if n < 10:
    return True
  q = str(n)
  for a in range(len(q)-1):
    if int(q[a]) > int(q[a+1]):
      return False
  return True

for a in range(t):
  n = raw_input()
  if is_tidy(int(n)) == True:
    print "Case #%d: %d" % (a+1,int(n))
    continue

  q = n[0:2]
  q = int(q)
  for x in range(q,0,-1):
    if is_tidy(x) == True:
      ans = str(x) + "9" * (len(n)-2)
      if int(ans) < int(n):
        print "Case #%d: %d" % (a+1,int(ans))
        break

