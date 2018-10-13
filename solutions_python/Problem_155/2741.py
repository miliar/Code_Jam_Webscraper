def solve():
    sm = 0
    ans = 0
    for i,e in enumerate(s):
        if e==0:
            continue
        if i>sm:
            ans = ans + (i-sm) 
            sm = i + e
        else:
            sm = sm + e
    return ans

T = int(raw_input())

for i in range(T):
  N , s = raw_input().split()
  s = [ int(c) for c in s ]
  print "Case #%d: %s"%(i+1,solve())
