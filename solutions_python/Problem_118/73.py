import sys
import bisect

def reverse(a, m=-1):
  rs = str(a)[::-1]
  while len(rs) < m: rs = rs + '0'
  return int(rs)

def makePal(val, m, d=-1):
  vr = reverse(val, m)
  if d != -1: vr = 10*vr + d
  vr *= (10 ** m)

  return vr+val

def verify(p): return isPal(p) and isPal(p*p)

def isPal(p): return p == reverse(p)

def genPalsR(k, m, val):
  # current palindrome has m most.sig. digits (rev. val) and m least sig. digits (val)
  if (k-m-m == 1):
    for d in xrange(10):
      p = makePal(val, m, d)
      if verify(p): yield p
  elif (k-m-m == 0):
    p = makePal(val, m)
    if verify(p): yield p
  else:
    for d in xrange(10):
      suff = val + d*(10**m)
      suff2 = pow(suff, 2, 10**(m+1))

      suff2 = reverse(suff2, m+1)

      targetL = suff2 * (10**m)
      targetH = (suff2+1) * (10**m)

      pref = reverse(suff, m+1)
      lo = (pref*pref)
      hi = ((pref+1)*(pref+1))

      if (lo < targetH) and (targetL < hi):
        ans = list(genPalsR(k, m+1, suff))
        if not ans: break
        else:
          for v in ans:
            yield v
      else: break

def genPals(k):
  # first dig is 1,2,3
  for i in xrange(1,4):
    for v in genPalsR(k, 1, i):
      yield v

def main(MAX_K=100):
  pals = [1,4,9]
  for k in xrange(2, 1+(MAX_K // 2)):
    pals.extend(p*p for p in genPals(k))

  nc = int(raw_input())
  for curC in xrange(1, 1+nc):
    a, b = map(int, raw_input().split())

    ka = bisect.bisect_left(pals, a)
    kb = bisect.bisect_right(pals, b)

    print "Case #{0}: {1}".format(curC, kb-ka)

if __name__ == "__main__": sys.exit(main())

