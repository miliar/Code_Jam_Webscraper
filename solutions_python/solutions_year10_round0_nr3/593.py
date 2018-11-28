T = int(raw_input())

def find(k,groups,l):
  if sum(groups[0:l]) <= k:
    #print "l=",l," g=",sum(groups[0:l])
    return l
  return find(k,groups,l-1)


for t in xrange(T):
  ans = 0
  R,k,N = map(int,raw_input().split())
  groups = map(int,raw_input().split())
  
  for r in xrange(R):
    i = find(k,groups,len(groups))
    ans += sum(groups[0:i])
    tail = groups[0:i]
    head = groups[i::]
    groups = head
    groups.extend(tail)
  
  print "Case #"+str(t+1)+":",ans