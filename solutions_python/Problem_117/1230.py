import sys

def solution(input, m, n):
  M = map(max, input)
  N = []
  for x in range(n):
    N.append(max(map(lambda y: y[x], input)))

  for x in range(m):
    for y in range(n):
      if input[x][y] not in [M[x], N[y]]:
        return "NO"

  return "YES"

def parse(line):
  return map(int, line.split())

lines = map(parse, sys.stdin.readlines())

T = lines[0][0]
lines = lines[1:]
for x in range(T):
  m,n = lines[0]
  print "Case #%d: "%(x+1) + solution(lines[1:1+m], m, n)
  lines = lines[m+1:]
