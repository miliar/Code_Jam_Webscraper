#!/usr/bin/python

import array

def append1(h, key, value):
  if (not h.has_key(key)):
    h[key] = list()
  h[key] = h[key] + value

def append(ll, h, key, value):
  h[key] = h[key] + len(value)
  if not key in ll:
    ll.append(key)

def solve(n, k):
  #print "DEBUG: solve(n={}, k={}) called.".format(n, k)
  maax = -1
  miin = -1
  h = array.array('i', [0] * (n + 1))
  ll = list()
  #h[n] = [1]
  h[n] = 1
  ll.append(n)
  for i in xrange(k):
    top = max(ll)
    #print "DEBUG: i={}, top={}, ll={}".format(i, top, ll)
    if top % 2 == 1: #odd
      append(ll, h, (top - 1) / 2, [1, 1])
      maax = miin = (top - 1) / 2
      #print "DEBUG: odd. Two same parts of length {}".format(maax)
    else:
      append(ll, h, top / 2, [1])
      append(ll, h, top / 2 - 1, [1])
      maax = top / 2
      miin = top / 2 - 1
      #print "DEBUG: even. Two parts of length {} and {}".format(maax, miin)

    # remove one enry from h[top] since it is split in two!
    #h[top].remove(1)
    h[top] = h[top] - 1
    if h[top] == 0:
      #del(h[top])
      #h[top] = 0
      ll.remove(top)
      #ll[:] = [item for item in ll if item != top]
      #print "DEBUG: Removing {} from ll. New ll={}".format(top, ll)

  #print "DEBUG: solve(n={}, k={}) returning maax={}, minn={}.".format(n, k, maax, miin)
  return maax, miin

def main():
  # read a line with a single integer
  t = int(raw_input())
  for i in xrange(1, t + 1):
    # read a list of integers, 1 in this case
    n, k = [int(s) for s in raw_input().split(" ")]
    maax, miin = solve(n, k)
    result = "Case #{0}: {1} {2}".format(i, maax, miin)
    print result

main()
