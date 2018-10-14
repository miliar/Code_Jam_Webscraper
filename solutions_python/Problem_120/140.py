r = 0
tot = 0

def binary(start, end):
  if(start==end):
      return start
  mid = (start+end+1)/2
  v = 2*mid*mid + 2*mid*(r-1) + mid
  if(v>tot):
    return binary(start,mid-1)
  return binary(mid,end)

t = int(raw_input())
for i in range(1,t+1):
  r,tot = raw_input().split(' ')
  r=int(r)
  tot=int(tot)
  print 'Case #%d: %d' % (i, binary(1,tot))
