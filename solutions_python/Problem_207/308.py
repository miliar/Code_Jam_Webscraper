#!/usr/bin/env python3

from sys import stdin as I

def solve():
  N, R, O, Y, G, B, V = map(int, I.readline().split())
  # only green & red
  if O + Y + B + V == 0:
    if R == G:
      return 'RG' * R
    else:
      return 'IMPOSSIBLE'

  # only orange & blue
  if R + Y + G + V == 0:
    if B == O:
      return 'OB' * O
    else:
      return 'IMPOSSIBLE'

  # only yellow & violet
  if R + O + G + B == 0:
    if Y == V:
      return 'YV' * Y
    else:
      return 'IMPOSSIBLE'

  # we have more than two colors
  if O > 0:
    if O >= B:
      return 'IMPOSSIBLE'
    else:
      Bs = ['BO' * O + 'B'] + ['B'] * (B - O - 1)
  else:
    Bs = ['B'] * B

  if V > 0:
    if V >= Y:
      return 'IMPOSSIBLE'
    else:
      Ys = ['YV' * V + 'Y'] + ['Y'] * (Y - V - 1)
  else:
    Ys = ['Y'] * Y

  if G > 0:
    if G >= R:
      return 'IMPOSSIBLE'
    else:
      Rs = ['RG' * G + 'R'] + ['R'] * (R - G - 1)
  else:
    Rs = ['R'] * R

  if max([len(Rs), len(Ys), len(Bs)]) * 2 > N:
    return 'IMPOSSIBLE'

  S = ''
  last = None
  while len(Rs) + len(Bs) + len(Ys) != 0:
    X = filter(lambda x: x != last, [Rs, Bs, Ys])
    X = sorted(X, key=len, reverse=True)
    last = X[0]
    S += last.pop()
  if S[0] == S[-1]:
    return S[:-2] + S[-1] + S[-2]
  return S

T = int(I.readline())
for i in range(T):
  S = solve()
  print("Case #%i: %s" % (i + 1, S))
