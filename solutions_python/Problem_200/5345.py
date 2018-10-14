
def is_tidy(n):
  l = list(str(n))
  for i in xrange(0,len(l)-1):
    if l[i] <= l[i+1]:
      continue
    else:
      return False
  return True

t = {}

N = 1000

for i in xrange(1,N+1):
  for j in xrange(i,0,-1):
    if is_tidy(j):
      t[i] = j
      break

T = int(raw_input())
for i in xrange(T):
  j = raw_input()
  print "Case #%d: %d" % (i+1,t[int(j)])


