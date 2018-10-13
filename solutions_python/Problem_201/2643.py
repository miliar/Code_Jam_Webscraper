#!/usr/bin/env pypy3

import sys


def calcLsRs(state, i):
  Ls = 0
  for j in range(i - 1, -1, -1):
    if state[j]:
      break
    Ls += 1
  Rs = 0
  for j in range(i + 1, len(state)):
    if state[j]:
      break
    Rs += 1
  return Ls, Rs


def solve(N, K):
  state = [True] + [False] * N + [True]
  # print(state)

  for k in range(K):
    maxMinLsRs = -1
    maxMinLsRs_si = -1
    bestMinLsRs = -1
    maxMaxLsRs = -1
    maxMaxLsRs_si = -1
    bestMaxLsRs = -1
    for si in range(1, N + 1):
      if state[si]:
        continue

      Ls, Rs = calcLsRs(state, si)
      # print("si = ", si, "Ls = ", Ls, "Rs = ", Rs)
      minLsRs = min(Ls, Rs)
      maxLsRs = max(Ls, Rs)
      if minLsRs > maxMinLsRs:
        maxMinLsRs = minLsRs
        bestMinLsRs = minLsRs
        maxMaxLsRs = maxLsRs
        bestMaxLsRs = maxLsRs
        maxMinLsRs_si = si
        maxMaxLsRs_si = -1
        # print("maxMinLsRs_si = ", si)
      elif minLsRs == maxMinLsRs:
        if maxLsRs > maxMaxLsRs:
          maxMaxLsRs = maxLsRs
          bestMaxLsRs = maxLsRs
          maxMaxLsRs_si = si
          # print("maxMaxLsRs_si = ", si)

    # update state
    assert(1 <= maxMinLsRs_si <= N)
    if maxMaxLsRs_si != -1:
      assert(1 <= maxMaxLsRs_si <= N)
      state[maxMaxLsRs_si] = True
    else:
      state[maxMinLsRs_si] = True
    # print(state)

  return bestMaxLsRs, bestMinLsRs


if __name__ == "__main__":
  input_filepath = sys.argv[1]

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      N, K = map(int, next(input_file).split(" "))
      sol = solve(N, K)
      print("Case #%u: %u %u" % (i, sol[0], sol[1]))

    assert(i == T)
