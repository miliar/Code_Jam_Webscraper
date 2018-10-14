#! /usr/bin/env python

def solve(file):
  _A, _B, K = [int(s) for s in file.readline().split(' ')]
  A = max(_A, _B)
  B = min(_A, _B)
  total = 0
  for b in range(0, B):
    for a in range(b, A):
      for k in range(0, K):
        if (a & b) == k:
          if a < B and a != b:
            total += 2
          else:
            total += 1
          break
  return total


input = open('input.txt')
cases = int(input.readline())
output = open('output.txt', 'w')
for i in range(cases):
  res = solve(input)
  output.write("Case #%d: %s\n" % (i + 1, res))
output.close()
input.close()