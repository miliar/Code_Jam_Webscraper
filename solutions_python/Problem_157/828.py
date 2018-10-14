#!/usr/bin/python3
T = int(input())

table = {
    '1': {
      '1': '1',
      'i': 'i',
      'j': 'j',
      'k': 'k',
    },
    'i': {
      '1': 'i',
      'i': '-1',
      'j': 'k',
      'k': '-j'
    },
    'j': {
      '1': 'j',
      'i': '-k',
      'j': '-1',
      'k': 'i'
    },
    'k': {
      '1': 'k',
      'i': 'j',
      'j': '-i',
      'k': '-1'
    }
}

def mul(a, b):
  r = table[a[-1]][b[-1]]
  if len(a) + len(b) == 3:
    if len(r) == 2:
      return r[-1]
    else:
      return '-' + r
  else:
    return r

for t in range(1, T+1):
  L, X = map(int, input().split())
  S = input()

  a = '1'
  for s in S:
    a = mul(a, s)

  b = '1'
  for i in range(X % 4):
    b = mul(b, a)

  if b != '-1':
    print('Case #{}: NO'.format(t))
    continue

  cnt_i = 0
  c = '1'
  Xi = max(4, X)
  for s in Xi*S:
    cnt_i += 1
    c = mul(c, s)
    if c == 'i':
      break
  else:
    print('Case #{}: NO'.format(t))


  cnt_k = 0
  c = '1'
  for s in reversed(Xi*S):
    cnt_k += 1
    c = mul(s, c)
    if c == 'k':
      break
  else:
    print('Case #{}: NO'.format(t))
    continue

  if cnt_i + cnt_k < L * X:
    print('Case #{}: YES'.format(t))
  else:
    print('Case #{}: NO'.format(t))

