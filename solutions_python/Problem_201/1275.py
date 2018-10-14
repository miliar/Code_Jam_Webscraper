import math

def bisection(n, k):
  result = [n]
  for i in xrange(k):
    m = result.pop(0)
    r_n = math.floor(m/2)
    l_n = max(0,m - 1 - r_n)

    j = 0
    while j < len(result):
      if r_n > result[j]:
        break
      j = j + 1
    result.insert(j, r_n)
    while j < len(result):
      if l_n > result[j]:
        break
      j = j + 1
    result.insert(j, l_n)
  return result

def bisection_rec(n, k):
  if k == 0:
    return [n]
  else:
    r_n = math.floor(n/2)
    l_n = max(0,n - 1 - r_n)
    r_k = math.floor(k/2)
    l_k = k - 1 - r_k
    return bisection_rec(r_n, r_k) + bisection_rec(l_n, l_k)

if __name__ == '__main__':
  T = int(raw_input())
  cases_n = []
  cases_k = []
  for i in xrange(T):
    data = raw_input().split()
    
    cases_n.append(int(data[0]))
    cases_k.append(int(data[1]))

  for i in xrange(T):
    n = cases_n[i]
    k = cases_k[i]

    empty_rows = bisection_rec(n,k-1)
    longest_row = max(empty_rows)

    s_max = math.floor(longest_row/2)
    s_min = longest_row - 1 - s_max

    print 'Case #%d: %d %d' % (i+1, s_max, s_min) 

    
