def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x:
            hi = mid
        else:
            return mid
    return lo

def ge(A,x) : 
  i = binary_search(A,x)
  n = len(A)
  return n - i


T = int(raw_input())
for i in range(T) : 
  L = [int(x) for x in raw_input().split()]
  N = L[0]
  S = L[1]
  p = L[2]
  L = L[3:]
  
  L = sorted(L)
  ans = ge(L,3*p-2)
  if p > 1: 
    x = ge(L,3*p-4)
   
    t = x - ans
    if S >= t : ans += t
    else : ans += S
  
  print "Case #%d: %d" %(i+1, ans)

      
