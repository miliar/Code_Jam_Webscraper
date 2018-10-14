#!/usr/bin/env python
# coding: utf-8

MAX = 2*1000*1000+1

num = [[] for i in range(1, MAX+5)]

for i in range(1, MAX):
  global n
  s = str(i)
  l = len(s)
  for j in range(1, l):
    if s[j] != '0':
      rec = int(s[j:] + s[:j])
      if rec < MAX:
        num[i].append(rec)

def solve(A, B):
  ret = 0
  for i in range(A, B+1):
    st = set()
    for v in num[i]:
      if i < v <= B:
        st.add((i, v))
    ret += len(st)
  return ret

for case in range(int(input())):
  A, B = map(int, input().split())
  print("Case #{0}: {1}".format(case+1, solve(A, B)))
