from collections import OrderedDict

def checked_add(Q, size, nb):
  if size in Q:
    Q[size] += nb
  else:
    Q[size] = nb

_T = int(raw_input())
for _t in range(1, _T+1):
  N, K = map(int, raw_input().split())

  Q = OrderedDict()
  Q[N] = 1
  k = 0

  while k < K:
    size, nb = Q.popitem(last = False)
    k += nb
    if size % 2 == 1:
      checked_add(Q, size/2, nb * 2)
    else:
      checked_add(Q, size/2, nb)
      checked_add(Q, size/2 - 1, nb)
  if size % 2 == 1:
    res = '{} {}'.format(size/2, size/2)
  else:
    res = '{} {}'.format(size/2, size/2-1)

  print 'Case #{}: {}'.format(_t, res)
