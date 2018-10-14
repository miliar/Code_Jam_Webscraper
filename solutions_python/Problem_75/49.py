import sys, os, re


T = int(sys.stdin.readline())

for case_ in range(T):
  sys.stdout.write('Case #{0}: '.format(case_ + 1))
  ss = sys.stdin.readline()[:-1].split(' ')
  C = int(ss[0])
  D = int(ss[C + 1])
  N = int(ss[C + D + 2])
  query = ss[C + D + 3]
  stack = []
  Cs = {}
  Ds = []
  for i in range(C):
    pattern = ss[i + 1]
    Cs[pattern[0] + pattern[1]] = pattern[2]
    Cs[pattern[1] + pattern[0]] = pattern[2]

  for i in range(D):
    pattern = ss[i + C + 2]
    Ds.append(pattern[0] + pattern[1])
    Ds.append(pattern[1] + pattern[0])

  for c in query:
    stack.append(c)
    if (len(stack) > 1):
      last = ''.join(stack[-2:])
      if last in Cs:
        stack = stack[:-2]
        stack.append(Cs[last])
      for d in Ds:
        if d[0] in stack and d[1] in stack:
           stack = []
  sys.stdout.write('[')
  if len(stack) != 0:
    sys.stdout.write(stack[0])
  for i in range(1, len(stack)):
    sys.stdout.write(', ' + stack[i])
  print(']')
