import sys
import math

def checkpal(kk):
  l = str(kk)
  r = str(kk)[::-1]
  if l == r:
    return 1
  else:
    return 0

def counteven(l, A, B):
  maxi = int(10 ** l)
  st = maxi/10
  cnt = 0
  for i in range(st, maxi):
    k = int(str(i) + str(i)[::-1])
    kk = k**2
    if A<=kk and kk<=B and len(str(k)) == l*2:
      cnt += checkpal(kk)
  return cnt

def countodd(l, A, B):
  if l==0:
    return countoddsingle(l, A, B)
  else:
    return countoddmulti(l, A, B)

def countoddsingle(l, A, B):
  cnt = 0
  for k in range(10):
    kk = k**2
    if A<=kk and kk<=B:
      cnt += checkpal(kk)
  return cnt

def countoddmulti(l, A, B):
  cnt = 0
  maxi = (int)(10 ** (l-1))
  st = maxi/10
  for i in range(st, maxi):
    for j in range(10):
      k = int(str(i) + str(j) + str(i)[::-1])
      kk = k**2
      if A<=kk and kk<=B and len(str(k)) == l*2-1:
        cnt += checkpal(kk)
  return cnt

def solve():
  line = sys.stdin.readline().split()
  A = int(line[0])
  B = int(line[1])
  blen = len(str(int(math.sqrt(B)+.99)))
  evenlen = blen / 2
  oddlen = (blen + 1) / 2

  cnt = 0
  for even in range(evenlen+1):
     cnt += counteven(even, A, B)
  for odd in range(oddlen+1):
     cnt += countodd(odd, A, B)

  return cnt

def main():
  T = (int)(sys.stdin.readline())
  for t in range(T):
      s = solve()
      print "Case #%d: %d" % (t+1, s)

if __name__ == "__main__":
    main()
