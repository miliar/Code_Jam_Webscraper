from fractions import gcd
def main():
  for case in range(input()):
    x = raw_input().split()
    n = int(x[0])
    if n == 2:
      # k1 < k2
      k1,k2 = map(long,x[1:])
      if k1 > k2:
        k1,k2 = k2,k1
      d = k2 - k1
      # print d
      # m = k1 & d-1
      m = k1 % d
      # print m
      if m == 0:
        r = 0
      else:
        r = d - m
    else:
      # n == 3
      k1,k2,k3 = map(long,x[1:])
      d1 = abs(k1-k2)
      d2 = abs(k2-k3)
      d3 = abs(k1-k3)
      d = gcd(d1, gcd(d2, d3))
      
      m = k1 % d
      if m == 0:
        r = 0
      else:
        r = d - m
    print 'Case #%s: %s' % (case + 1, r )
main()