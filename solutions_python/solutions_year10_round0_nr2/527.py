
def gcd(a,b):
  if b: return gcd(b,a%b)
  return a

C=int(raw_input())
for c in range(C):
  line=map(int,raw_input().split())
  g=0
  for i in range(1,len(line)-1):
    g=gcd(g,abs(line[i]-line[i+1]))
  print "Case #"+str(c+1)+": "+str((-line[1])%g).rstrip("L")
