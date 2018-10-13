#!/usr/bin/python3
# A: Oversized Pancake Flipper

from collections import deque

T = int(input())
for case in range(T):
  S, K = input().split(' ')
  K = int(K)

  L = len(S)
  MASK = (1 << K) - 1

  state = 0
  for i in range(L):
    state |= ('-' == S[i]) << i

  queue = deque(((state, 0),))
  seen = set()
  result = 'IMPOSSIBLE'
  while len(queue):
    ele, moves = queue.popleft()

    if 0 == ele:
      result = moves
      break

    seen.add(ele)
    for i in range(L - K + 1):
      new_ele = ele ^ (MASK << i)
      if 0 == new_ele:
        result = moves + 1
        break
      elif new_ele not in seen:
        seen.add(new_ele)
        queue.append((new_ele, moves + 1))

    if result is not 'IMPOSSIBLE':
      break

  print('Case #%d: %s' % (case + 1, result))
