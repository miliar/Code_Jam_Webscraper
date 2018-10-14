#!/bin/python2

import fileinput

def read_int(lines, cur):
  return (int(lines[cur]), cur + 1)

def read_matr(lines, cur):
  matr = [map(int, lines[cur+i].split()) for i in xrange(4)]
  return (matr, cur + 4)

lines = [line for line in fileinput.input()]

T = int(lines[0])
cur = 1
for i in xrange(1, T+1):
  n1, cur = read_int(lines, cur)
  m1, cur = read_matr(lines, cur)
  n2, cur = read_int(lines, cur)
  m2, cur = read_matr(lines, cur)

  ans = set(m1[n1-1]).intersection(set(m2[n2-1]))
  ans = list(ans)
  if len(ans) == 1:
    msg = str(ans[0])
  elif len(ans) == 0:
    msg = "Volunteer cheated!"
  elif len(ans) > 1:
    msg = "Bad magician!"

  print ("Case #%i: " + msg) % (i,)
