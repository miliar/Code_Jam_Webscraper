from sys import stdin
from fractions import gcd

def lcm(a, b):
  return (a//gcd(a, b))*b

def main():
  nt=int(stdin.readline().strip())
  for t in range(nt):
    b,n=[int(x) for x in stdin.readline().strip().split()]
    m=[int(x) for x in stdin.readline().strip().split()]
    #print("\n",b, n, m)
    if n<=b:
      print("Case #{0}: {1}".format(t+1, n))
      continue
    a=1
    for i in range(b):
      a=lcm(a, m[i])
    ctg=0
    for i in range(b):
      ctg=ctg+(a//m[i])
    #print("a", a, "ctg", ctg)
    hi, lo=0,0
    if (ctg+b>=n):
      lo, hi=0, a
    else:
      lo, hi=0, ((n//ctg)+1)*a+1
    #print(lo, hi)
    while hi-lo>1:
      mid=lo+(hi-lo)//2
      if mid==0: break
      #print(mid)
      ct=b+ctg*((mid)//a)
      for i in range(b):
        ct+=((mid%a)//m[i])
      if ct>=n:
        hi=mid
      else:
        lo=mid
    #print("-->",lo, hi)
    ct=b+ctg*((lo)//a)
    for i in range(b):
      ct+=((lo%a)//m[i])
    #print("ct", ct)
    for i in range(b):
      #print(ct, m[i])
      if (hi%m[i])==0:
        ct+=1
      if ct==n:
        break
    print("Case #{0}: {1}".format(t+1, i+1))


main()
