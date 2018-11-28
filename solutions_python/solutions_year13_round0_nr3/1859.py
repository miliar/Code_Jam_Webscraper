from sympy import sqrt as ssqrt
from sympy import ceiling as sceiling
from sympy import N
f = open('input', 'r')
t = int(f.readline())
f1 = open('output', 'w')
for tt in xrange(t):
  [a, b] = map(int, f.readline().split())
  aSqrt = N(ssqrt(a))
  aSqrtCeil = sceiling(aSqrt)
  a1 = aSqrtCeil * aSqrtCeil
  n = 0
  while (a1 <= b):
    la1 = list(str(a1))
    laSqrtCeil = list(str(aSqrtCeil))
    if ((la1 == la1[::-1]) and (laSqrtCeil == laSqrtCeil[::-1])):
      n += 1
    a1 += 2*aSqrtCeil+1
    aSqrtCeil += 1

  f1.write('Case #{0}: {1}\n'.format(tt+1, n))
f.close()
f1.close()
