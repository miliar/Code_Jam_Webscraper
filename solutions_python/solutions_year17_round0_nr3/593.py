#!/bin/env python3

def f(a, na, b, nb, k):
  if k <= na:
    return a
  elif k <= na + nb:
    return b

  ra = a // 2;
  rb = (b - 1) // 2;
  
  rna = na;
  rnb = nb;

  if (a - 1) // 2 == ra:
    rna += na
  else:
    rnb += na

  if b // 2 == ra:
    rna += nb
  else:
    rnb += nb

  rk = k - na - nb;

  return f(ra, rna, rb, rnb, rk)


def solve(n, k):
  if k == 1:
    return ((n - 1) // 2, n // 2)

  s = f(n // 2, 1, (n - 1) // 2, 1, k - 1)
  return ((s - 1) // 2, s // 2)

def main():
  T = int(input())
  for test_index in range(1, T + 1):
    test = input().split()
    n = int(test[0])
    k = int(test[1])
    a, b = solve(n, k)
    print("Case #%d: %d %d" % (test_index, b, a))

if __name__ == '__main__':
  main()
