import fileinput
from math import ceil

input = fileinput.input()

T = int(input.readline())

for i in range(T):
  line = input.readline()
  N, S, p, *scores = map(int,line.strip().split(' '))
  result = 0
  for s in scores:
    if s == 0:
      possible_highs = (0,0)
    elif s == 1:
      possible_highs = (1,1)
    elif s == 2:
      possible_highs = (1,1)
    else:
      avg = s / 3
      possible_highs = (ceil(avg),ceil(avg)) if s%3 == 1 else (ceil(avg)+1,ceil(avg))

    if possible_highs[1] >= p:
      result += 1
    elif S > 0 and possible_highs[0] >= p:
      S -= 1
      result += 1

  print("Case #{0}: {1}".format(i + 1, result))
