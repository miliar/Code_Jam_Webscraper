#!/usr/bin/python

def solve(L, t, N, a):
  time = 0
  i = 0
  while i < len(a) and  time + a[i]*2 < t:
    time += a[i] * 2
    i += 1
  #print time, a
  if i >= len(a):
    return time
  d = (t - time) / 2
  #print d
  time = t
  a = sorted([a[i] - d] + a[i+1:], reverse=True)
  j = 0
  i = 0
  while i < len(a) and j < L:
    time += a[i]
    j += 1
    i += 1
  while i < len(a):
    time += a[i] * 2
    i += 1
  #print "here"
  return time


def main():
  num_tests = int(raw_input())
  for test in xrange(num_tests):
    v = map(int, raw_input().split())
    L, t, N, C = v[0], v[1], v[2], v[3]
    a = []
    for i in xrange(N):
      a.append(v[i % C + 4])
    sol = solve(L, t, N, a)
    print "Case #{0}: {1}".format(test+1, sol)
main()
