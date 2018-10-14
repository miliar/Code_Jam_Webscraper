def min_res(a,b):
  if (a[1] < b[1]):
    return a
  else:
    if (a[1] == b[1]):
      if (a[0] < b[0]):
        return a
      else:
        return b
    else:
      return b


def solution(n,k):
  if (k == 1):
    return (n/2,n-n/2-1)
  else:
    if (k == 0):
      return (n,n)
    else:
      if ((n%2) == 1):
        return solution(n/2,k/2)
      else:
        return min_res(solution(n/2,k/2),solution((n-n/2-1),(k-k/2-1)))


t = int(raw_input())
for i in xrange(1, t + 1):
  n,k = (int(s) for s in raw_input().split(' '))
  res = solution(n,k)
  res_str = "%d %d" %(res)
  case_str = "Case #%d: " %i
  print case_str + res_str
