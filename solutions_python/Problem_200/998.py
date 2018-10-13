x = int(input())
for num in range(1, x + 1):
  curr = list(input());
  for i in range(len(curr) - 2, -1, -1):
    if curr[i] > curr[i + 1]:
      curr[i] = str(int(curr[i]) - 1);
      for j in range(i + 1, len(curr)):
        curr[j] = '9'
  print(str(int("".join(curr))));
