from heapq import heappush, heappop

def MyFunc(act1, act2):
  N = 1440
  bitmap = [None] * N
  missing = [None] * N
  trueBalance = 720
  falseBalance = 720
  rtn = 0
  last_C = set()
  last_D = set()
  for C, D in act1:
    for j in range(C, D):
      bitmap[j] = False
    if C not in last_D and D not in last_C: rtn += 1
    last_D.add(D)
    last_C.add(C)
    falseBalance -= (D - C)
  last_C = set()
  last_D = set()
  for C, D in act2:
    for j in range(C, D):
      bitmap[j] = True
    if C not in last_D and D not in last_C: rtn += 1
    last_D.add(D)
    last_C.add(C)
    trueBalance -= (D - C)
  # Fill in the missing pieces
  trueGap = []
  falseGap = []
  # rtn + # true gap + # false gap - # filled true gap - # filled false gap
  # Find the leading gap
  start_idx = 0
  while start_idx < N:
    if bitmap[start_idx] is None:
      start_idx += 1
    else:
      break
  # Find the trailing gap
  end_idx = N - 1
  while end_idx >= 0:
    if bitmap[end_idx] is None:
      end_idx -= 1
    else:
      break
  gapSize = N - 1 + start_idx - end_idx
  if gapSize > 0 and bitmap[start_idx] == bitmap[end_idx]:
    rtn += 1
    if bitmap[start_idx] is True:
      heappush(trueGap, gapSize)
    else:
      heappush(falseGap, gapSize)
  if gapSize == 0 and bitmap[start_idx] == bitmap[end_idx]:
    rtn -= 1
  idx = start_idx
  lastChar = bitmap[start_idx]
  while idx < end_idx:
    if bitmap[idx] is lastChar:
      idx += 1
    elif bitmap[idx] is None:
      gapStart = idx
      while bitmap[idx] is None:
        idx += 1
      if bitmap[idx] is not lastChar:
        # not a gap actually
        lastChar = bitmap[idx]
      else:
        # Actually a gap
        rtn += 1
        gapSize = idx - gapStart
        if lastChar is True:
          heappush(trueGap, gapSize)
        if lastChar is False:
          heappush(falseGap, gapSize)
    else:
      lastChar = bitmap[idx]
      idx += 1
  # print(rtn)
  # print(trueGap)
  # print(falseGap)
  # print(trueBalance)
  # print(falseBalance)
  # Fill the gaps as long as I can
  while trueGap and trueBalance >= trueGap[0]:
    rtn -= 2
    trueBalance -= trueGap[0]
    heappop(trueGap)
  while falseGap and falseBalance >= falseGap[0]:
    rtn -= 2
    falseBalance -= falseGap[0]
    heappop(falseGap)
  return rtn

if __name__ == '__main__':
  T = int(input())
  for i in range(1, T + 1):
    A, B = map(int, input().split(' '))
    act1 = []
    act2 = []
    for j in range(A):
      C, D = map(int, input().split(' '))
      act1.append((C, D))
    for j in range(B):
      C, D = map(int, input().split(' '))
      act2.append((C, D))
    output = MyFunc(act1, act2)
    print('Case #{}: {}'.format(i, output))
