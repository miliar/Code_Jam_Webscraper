def SimpleGetArrangement(R, Y, B):
  if R == 0 and Y == 0 and B == 0: return ''
  if R == 1 and Y == 0 and B == 0: return 'R'
  if R == 0 and Y == 1 and B == 0: return 'Y'
  if R == 0 and Y == 0 and B == 1: return 'B'
  if R + Y < B or Y + B < R or B + R < Y: return None
  if R + Y == B:
    return 'RB' * R + 'YB' * Y
  if Y + B == R:
    return 'YR' * Y + 'BR' * B
  if B + R == Y:
    return 'BY' * B + 'RY' * R
  if (R + Y + B) % 2 == 0:
    x = (R + B - Y) // 2
    y = (R + Y - B) // 2
    z = (B + Y - R) // 2
    return 'RB' * x + 'RY' * y + 'BY' * z
  else:
    x = (R + B - Y - 1) // 2
    y = (R + Y - B + 1) // 2
    z = (B + Y - 1 - R) // 2
    return 'RB' * x + 'RY' * y + 'BY' * z + 'B'

def ValidateArrangement(N, rtn):
  # check validity
  assert N == len(rtn)
  blacklist = ['RR', 'OO', 'YY', 'GG', 'BB', 'VV', 'RO', 'OR', 'YO', 'OY', 'YG', 'GY', 'BG', 'GB', 'RV', 'VR', 'BV', 'VB']
  if N > 1:
    for i in range(N):
      assert rtn[i] + rtn[(i + 1) % N] not in blacklist

def GetArrangement(N, R, O, Y, G, B, V):
  if R < G or Y < V or B < O: return 'IMPOSSIBLE'
  if R == G > 0:
    if O + Y + B + V == 0: return 'RG' * R
    else: return 'IMPOSSIBLE'
  if Y == V > 0:
    if R + O + G + B == 0: return 'YV' * Y
    else: return 'IMPOSSIBLE'
  if B == O > 0:
    if R + Y + G + V == 0: return 'BO' * B
    else: return 'IMPOSSIBLE'
  if O + Y + B + V == 0:
    if R > B: return 'IMPOSSIBLE'
  if R + O + G + B == 0:
    if Y > V: return 'IMPOSSIBLE'
  if R + Y + G + V == 0:
    if B > O: return 'IMPOSSIBLE'
  # Solve sub-problem
  rtn = SimpleGetArrangement(R - G, Y - V, B - O)
  if rtn is None: return 'IMPOSSIBLE'
  else:
    rtn = list(rtn)
    if 'R' in rtn: rtn[rtn.index('R')] = 'R' + 'GR' * G
    if 'B' in rtn: rtn[rtn.index('B')] = 'B' + 'OB' * O
    if 'Y' in rtn: rtn[rtn.index('Y')] = 'Y' + 'VY' * V
    return ''.join(rtn)

T = int(input())
for i in range(1, T + 1):
  N, R, O, Y, G, B, V = map(int, input().split(' '))
  arrangement = GetArrangement(N, R, O, Y, G, B, V)
  if arrangement != 'IMPOSSIBLE':
    ValidateArrangement(N, arrangement)
  print('Case #{}: {}'.format(i, arrangement))

# cache = dict()
# for r in range(10):
#   for y in range(10):
#     for b in range(10):
#       cache[(r, y, b)] = GetArrangement(r + y + b, r, 0, y, 0, b, 0)
