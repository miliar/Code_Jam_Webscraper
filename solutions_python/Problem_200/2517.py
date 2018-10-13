t = int(input())
for case in range(1, t + 1):

  n = [int(c) for c in input()]
  last = [n[-1]]
  
  for i in range(len(n) - 2, -1, -1):
  	if (n[i] > last[-1]):
  		last = [9] * len(last)
  		last.append(9 if n[i] == 0 else n[i]-1)
  	else:
  		last.append(n[i])
  
  if (last[-1] == 0): last.pop()

  print("Case #{}: {}".format(case, ''.join(
  	[str(c) for c in last[::-1]])))