from pdb import set_trace

def flip(row, k):
  res, i = 0, 0
  while i < len(row):
    if row[i] == '+':
      i += 1
      continue

    if i + k > len(row): return 'IMPOSSIBLE'
    row[i:i + k] = ''.join(map(lambda c: '-' if c == '+' else '+', row[i:i + k]))
    res += 1

  return res

def smart_flip(n, k, npancakes):
  r, nshift = 0, 0

  while nshift < npancakes:
    if n & 1:
      n >>= 1
      nshift += 1
      continue

    n ^= (1 << k) - 1
    r += 1

  if n > 0: return 'IMPOSSIBLE'
  return r

def as_number(string):
  return int(''.join(map(lambda c: '1' if c == '+' else '0', string)), 2)

if __name__ == '__main__' :
  import sys
  T = int(sys.stdin.readline())
  for i in range(1, T + 1):
    row, k = sys.stdin.readline().split(' ')
    npancakes = len(row)
    k = int(k)
    print('Case #{}: {}'.format(i, smart_flip(as_number(row), k, npancakes)))
