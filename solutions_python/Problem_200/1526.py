#!/usr/bin/python3

def is_tidy(n):
  last_c = "0"
  for c in str(n):
    if last_c > c:
      return False
    last_c = c
  return True

def test():
  result = 0
  def AddResult(n):
    nonlocal result
    if is_tidy(n):
      result = max(result, n)
  n = int(input())
  s = str(n)
  for i in range(len(s)):
    c = int(s[i])
    if c > 0:
      AddResult(int(s[:i] + str(c - 1) + "9" * len(s[i+1:])))
  AddResult(n)
  return result

t = int(input())

for i in range(t):
  print("Case #{}: {}".format(i + 1, test()))
