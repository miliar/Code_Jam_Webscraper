#!/usr/bin/env python3

################################################################################

def read_int():
  return int(input())

def read_words():
  return input().split()

def read_ints():
  return list(map(int,read_words()))

def read_floats():
  return list(map(float,read_words()))

################################################################################

def computeWar(n,k):
  ns = sorted(n, reverse=True)
  ks = sorted(k, reverse=True)

  size = len(ns)
  j = 0

  score = 0
  for kv in ks:
    while j<size and ns[j] > kv:
      j+=1
      score+=1
    j+=1

    if j >= size:
      break

  return score

def computeDeceit(n,k):
  ns = sorted(n)
  ks = sorted(k)

  m = 0
  for kv in ns:
    if kv > ks[m]:
      m += 1

  return m

def solve(n,k):
  w = computeWar(n,k)
  d = computeDeceit(n,k)
  return (d,w)


if __name__ == "__main__":
    T = read_int()
    for c in range(T):
        I = input().strip()
        n = read_floats()
        k = read_floats()
        (n,d) = solve(n,k)
        print("Case #{}: {} {}".format(c+1,n,d))
