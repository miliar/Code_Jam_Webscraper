def snapper(n,k):
  if ((2**(n-1))&k)>0 and (k+1)%2**(n-1)==0:
    return "ON"
  else:
    return "OFF"

N = int (raw_input())

for n in range(1,N+1):
  inp = [int(i) for i in raw_input().split()]
  #print inp
  print "Case #"+str(n)+": "+snapper(inp[0], inp[1])
