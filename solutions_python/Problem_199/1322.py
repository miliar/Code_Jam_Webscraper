#!/usr/bin/python3
num_cases = int(input())
for i in range(0,num_cases):
  data = input().split()
  cakes = list(data[0])
  flipper = int(data[1])
  flips = 0
  impossible = False
  cakes_length = len(cakes)
  for c in range(0,cakes_length):
    if cakes[c] == '-':
      if c + flipper > cakes_length:
        impossible = True
        break
      flips += 1
      cakes[c] = '+'
      for cake in range(c + 1,c + flipper):
        if cakes[cake] == '-':
          cakes[cake] = '+'
        else:
          cakes[cake] = '-'
  result = flips
  if impossible:
    result = 'IMPOSSIBLE'
  print("Case #{}: {}".format(i + 1, result))
