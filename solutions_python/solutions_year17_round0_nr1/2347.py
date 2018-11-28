t = int(input())

for i in range(1, t + 1):
  [s, k] = input().split(" ")
  k = int(k)
  a = [0 if c == '+' else 1 for c in s]

  nflip = 0
  for ci in range(len(a) - k + 1):
  	if (0 == sum(a)): break

  	if (a[ci] > 0):
  		nflip += 1

  		for ki in range(k):
  			a[ci+ki] = 0 if a[ci+ki] == 1 else 1

  print("Case #{}: {}".format(i, nflip if 0 == sum(a) else 'IMPOSSIBLE'))