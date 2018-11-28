import sys

import mpmath
import operator

def primes(n):
  """ returns a list of prime numbers from 2 to < n """
  if n < 2:  return []
  if n == 2: return [2]
  # do only odd numbers starting at 3
  s = range(3, n+1, 2)
  # n**0.5 may be slightly faster than math.sqrt(n)
  mroot = n ** 0.5
  half = len(s)
  i = 0
  m = 3
  while m <= mroot:
    if s[i]:
      j = (m * m - 3)//2
      print j
      print "--"+str(len(s))
      s[j] = 0
      while j < half:
          s[j] = 0
          j += m
    i = i + 1
    m = 2 * i + 3
  # make exception for 2
  return [2]+[x for x in s if x]
 

def solve(f):
    n, l, h = map(int, f.readline().split())
    notes = map(int, f.readline().split())
    m1 = min(notes)
    if l==1:
        return 1
    m = max(notes)
    f = 1
    print m
    p = primes(m+1)
    c=[]
    print notes
    for i in p:
        r = 0
        for j in notes:
            k=0
            while j % (i**k) == 0:
#                print j, i
                k+=1
            k-=1
            if k>r:
                r=k
        c.append(r)
#    print p
#    print c
    gcm = 1
    for j,i in enumerate(p):
        gcm *= i**c[j]
    if l<=max(notes):
        for x in range(l,h+1):        
            s=True
            for j in notes:
                if j>x and j%x!=0:
                    s = False
                    break
                if x>j and x%j!=0:
                    s = False
                    break
            if s:
                return x    
    print gcm, l, h
    div1 = l/gcm
    if l % gcm == 0 :
        return l
    elif (div1+1) * gcm<=h:
        return (div1+1) * gcm
    return False

if __name__ == "__main__":
    f = open(sys.argv[1])
    g = open(sys.argv[2],'w')
    t = int(f.readline())
    for _t in range(t):
        rez = solve(f)
        if not rez:            
            g.write("Case #%d: NO" % (_t+1))
        else:
            g.write("Case #%d: %d" % ((_t+1), rez))
        g.write("\n")
