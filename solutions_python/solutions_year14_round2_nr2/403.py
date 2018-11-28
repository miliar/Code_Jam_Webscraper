from base import main

def case():
  a, b, k = map(int, input().split())
  if k >= min(a, b):
    return a * b
  count = 0
  for i in range(a):
    for j in range(b):
      if (i & j) < k:
        count += 1

  return count

def msb(i):
  bit = 0
  while i:
    bit += 1
    i >>= 1
  return bit

if __name__ == '__main__': main(case)