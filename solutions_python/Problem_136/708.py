import sys

inp = sys.stdin

def solve(C,F,X):
  min_time=X/2.0
  initial=0.0
  n=1 # cost with n farm
  initial+=C/(2+F*(n-1))
  final = X/(2+F*n)
  while(initial+final<min_time):
    min_time = initial+final
    n+=1  
    initial+=C/(2+F*(n-1))
    final = X/(2+F*n)
  return min_time
    

T=int(inp.readline())
for t in range(1,T+1):
    C,F,X = [float(y) for y in inp.readline().split()]
    print "Case #%d: %s" % (t,solve(C,F,X))

