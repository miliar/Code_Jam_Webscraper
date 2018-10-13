#! /usr/bin/env python

def solve(file):
  N = int(file.readline())
  strings = [file.readline().strip() for i in range(0, N)]

  moves = 0
  current_index = [0] * N
  while True:
    repeats = [0] * N
    char = strings[0][current_index[0]]
    for n in range(0, N):

      i = current_index[n]
      while i < len(strings[n]):
        i += 1
        if i >= len(strings[n]) or strings[n][i] != strings[n][i-1]:
          break

      if strings[n][i-1] != char:
        return "Fegla Won"

      repeats[n] = (i - current_index[n])
      current_index[n] = i
    dst = int(round(reduce(lambda x, y: x + y, repeats) / len(repeats)))

    for r in repeats:
      moves += abs(dst - r)
    exhausted = 0

    for i in range(0, N):
      if current_index[i] >= len(strings[i]):
        exhausted += 1
    if exhausted == N:
      return moves
    elif exhausted > 0:
      return "Fegla Won"


input = open('input.txt')
cases = int(input.readline())
output = open('output.txt', 'w')
for i in range(cases):
  res = solve(input)
  output.write("Case #%d: %s\n" % (i + 1, res))
output.close()
input.close()