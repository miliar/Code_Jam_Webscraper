t = int(input())
for i in range(1, t + 1):
  number = [int(s) for s in input()]
  for k0 in range(len(number)-1,0,-1):
    if number[k0] < number[k0-1]:
      number[k0-1] -= 1
      for k1 in range(k0,len(number)):
        number[k1] = 9
  if number[0] == 0:
    del(number[0])
  print("Case #{}: {}".format(i, ''.join(str(e) for e in number)))