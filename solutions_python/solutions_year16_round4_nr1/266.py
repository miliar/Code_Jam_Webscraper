import sys


mem = {}


def check(s):
  if s in mem: return mem[s]
  return True


def gen(N, ns):
  if N == 0:
    if ns[0] > 0:
      ns[0] -= 1
      yield "P", "P"
      ns[0] += 1
    if ns[1] > 0:
      ns[1] -= 1
      yield "R", "R"
      ns[1] += 1
    if ns[2] > 0:
      ns[2] -= 1
      yield "S", "S"
      ns[2] += 1
  else:
    for left, w1 in gen(N - 1, ns):
      for right, w2 in gen(N - 1, ns):
        if w1 != w2:
          ans = left + right
          win = ""
          if w1 == "P" and w2 == "R": win = "P"
          if w2 == "P" and w1 == "R": win = "P"
          if w1 == "R" and w2 == "S": win = "R"
          if w2 == "R" and w1 == "S": win = "R"
          if w1 == "P" and w2 == "S": win = "S"
          if w2 == "P" and w1 == "S": win = "S"
          yield ans, win


def run(t):
  N, R, P, S = map(int, raw_input().split())

  res = None
  for ans, win in gen(N, [P, R, S]):
    res = ans
    break
  if not res:
    print('Case #{}: {}'.format(t, 'IMPOSSIBLE'))
  else:
    print('Case #{}: {}'.format(t, res))

T = int(raw_input())
for t in xrange(1, T + 1):
  run(t)
